import time
import os
import random
import string
import statistics
import concurrent.futures
import threading
import matplotlib.pyplot as plt
import pandas as pd
from tinydb import TinyDB
from odeta import localbase
import sqlite3

# --- CONFIGURATION ---
NUM_RECORDS = 500       # Records per thread
THREAD_COUNTS = [1, 5, 10, 20] # Concurrency levels
DB_FILE_ODETA = "bench_odeta.db"
DB_FILE_TINY = "bench_tiny.json"
RESULTS_FILE = "benchmark_results.csv"

# --- HELPER FUNCTIONS ---
def generate_payload():
    return {
        'name': ''.join(random.choices(string.ascii_letters, k=10)),
        'email': ''.join(random.choices(string.ascii_lowercase, k=5)) + "@example.com",
        'age': random.randint(18, 90),
        'active': True
    }

def clean_env():
    """Removes old database files and journals."""
    extensions = ['', '-wal', '-shm', '-journal']
    files = [DB_FILE_ODETA + ext for ext in extensions] + [DB_FILE_TINY]
    
    for f in files:
        if os.path.exists(f):
            try:
                os.remove(f)
            except OSError:
                pass
    time.sleep(0.5)

# --- DATABASE ADAPTERS ---

class OdetaAdapter:
    def __init__(self, filename):
        self.filename = filename
        self.local = threading.local()

    def _get_db(self):
        if not hasattr(self.local, 'db'):
            self.local.db = localbase(self.filename)
        return self.local.db

    def write(self, payload):
        db = self._get_db()
        table = db('users')
        return table.put(payload)

    def read(self, item_id):
        db = self._get_db()
        table = db('users')
        # Ensure item_id is a primitive to avoid crashes
        if isinstance(item_id, dict):
            # Fallback: try to find ID inside dict if it got passed incorrectly
            item_id = item_id.get('id') or item_id.get('_id')
        return table.get(item_id)

class TinyDBAdapter:
    def __init__(self, filename):
        self.filename = filename
        self.db = TinyDB(filename)

    def write(self, payload):
        return self.db.insert(payload)

    def read(self, item_id):
        return self.db.get(doc_id=item_id) if isinstance(item_id, int) else None

# --- BENCHMARK ENGINE ---

def worker_write(adapter, count):
    latencies = []
    ids = []
    
    # Debug: Print structure of first response to help diagnose issues
    first_run = True
    
    for _ in range(count):
        data = generate_payload()
        start = time.perf_counter()
        res = adapter.write(data)
        end = time.perf_counter()
        latencies.append((end - start) * 1000) # ms
        
        # Robust ID Extraction
        extracted_id = None
        if isinstance(res, dict):
            # Check common keys for ID
            extracted_id = res.get('id') or res.get('_id') or res.get('key') or res.get('uuid')
            
            # Debug print for the very first operation
            if first_run:
                print(f"DEBUG: ODETA put() response keys: {list(res.keys())}")
                if not extracted_id:
                     print(f"DEBUG: Could not find ID in response: {res}")
                first_run = False
                
        else:
            # Assume result is the ID (e.g., TinyDB returns int)
            extracted_id = res

        if extracted_id is not None:
            ids.append(extracted_id)
        else:
            # Fail safe: append the whole object but it will likely fail read test
            ids.append(res)
            
    return latencies, ids

def worker_read(adapter, ids):
    latencies = []
    for i in ids:
        try:
            start = time.perf_counter()
            adapter.read(i)
            end = time.perf_counter()
            latencies.append((end - start) * 1000)
        except Exception as e:
            # Catch errors to prevent crash, print first few
            if len(latencies) < 3: 
                print(f"Read Error on ID {i}: {e}")
    return latencies

def run_test_suite(db_type, adapter_cls, db_file):
    results = []
    print(f"--- Benchmarking {db_type} ---")
    
    for threads in THREAD_COUNTS:
        clean_env()
        try:
            adapter = adapter_cls(db_file)
            
            total_ops = threads * NUM_RECORDS
            print(f"  Running {threads} threads ({total_ops} total ops)...")

            # --- WRITE TEST ---
            start_global = time.perf_counter()
            all_write_latencies = []
            all_ids = []
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                futures = [executor.submit(worker_write, adapter, NUM_RECORDS) for _ in range(threads)]
                for f in concurrent.futures.as_completed(futures):
                    lats, ids = f.result()
                    all_write_latencies.extend(lats)
                    all_ids.extend(ids)
            
            end_global = time.perf_counter()
            duration = end_global - start_global
            write_throughput = total_ops / duration if duration > 0 else 0
            write_p95 = statistics.quantiles(all_write_latencies, n=20)[18] if all_write_latencies else 0

            # --- READ TEST ---
            random.shuffle(all_ids)
            chunk_size = max(1, len(all_ids) // threads)
            id_chunks = [all_ids[i:i + chunk_size] for i in range(0, len(all_ids), chunk_size)]
            
            start_global = time.perf_counter()
            all_read_latencies = []
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                futures = [executor.submit(worker_read, adapter, chunk) for chunk in id_chunks]
                for f in concurrent.futures.as_completed(futures):
                    all_read_latencies.extend(f.result())
                    
            end_global = time.perf_counter()
            duration = end_global - start_global
            read_throughput = total_ops / duration if duration > 0 else 0
            read_p95 = statistics.quantiles(all_read_latencies, n=20)[18] if all_read_latencies else 0

            results.append({
                "Database": db_type,
                "Threads": threads,
                "Write_Ops_Sec": write_throughput,
                "Write_Latency_P95": write_p95,
                "Read_Ops_Sec": read_throughput,
                "Read_Latency_P95": read_p95
            })
            print(f"    -> Writes: {int(write_throughput)}/s | Reads: {int(read_throughput)}/s")
        except Exception as e:
            print(f"    -> CRITICAL FAILURE in {db_type} at {threads} threads: {e}")

    return results

# --- MAIN EXECUTION ---

if __name__ == "__main__":
    all_results = []
    
    # Run Tests
    all_results.extend(run_test_suite("ODETA", OdetaAdapter, DB_FILE_ODETA))
    all_results.extend(run_test_suite("TinyDB", TinyDBAdapter, DB_FILE_TINY))
    
    # Save Data
    df = pd.DataFrame(all_results)
    df.to_csv(RESULTS_FILE, index=False)
    print(f"\nRaw data saved to {RESULTS_FILE}")

    # Generate Graphs
    print("\nGenerating Graphs...")
    
    # 1. Throughput
    plt.figure(figsize=(10, 6))
    for db in df['Database'].unique():
        subset = df[df['Database'] == db]
        plt.plot(subset['Threads'], subset['Write_Ops_Sec'], marker='o', label=f"{db} Write")
        plt.plot(subset['Threads'], subset['Read_Ops_Sec'], marker='x', linestyle='--', label=f"{db} Read")
    
    plt.title("Throughput vs Concurrency (Real Data)")
    plt.xlabel("Concurrent Threads")
    plt.ylabel("Ops / Sec")
    plt.legend()
    plt.grid(True)
    plt.savefig("real_throughput.png")
    
    # 2. Latency
    plt.figure(figsize=(10, 6))
    for db in df['Database'].unique():
        subset = df[df['Database'] == db]
        plt.plot(subset['Threads'], subset['Write_Latency_P95'], marker='o', label=f"{db} Write Latency")
    
    plt.title("P95 Write Latency vs Concurrency (Real Data)")
    plt.xlabel("Concurrent Threads")
    plt.ylabel("Latency (ms)")
    plt.legend()
    plt.grid(True)
    plt.savefig("real_latency.png")
    
    print("Graphs saved: real_throughput.png, real_latency.png")
    clean_env()