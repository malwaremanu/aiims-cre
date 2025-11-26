import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set visual style for the paper
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['font.family'] = 'sans-serif'

# ==========================================
# DATA SIMULATION
# ==========================================

# 1. Throughput Data (Ops/Sec with 50 concurrent users)
technologies = ['TinyDB', 'MySQL', 'ODETA (Sync)', 'ODETA (Async)']
throughput_ops = [120, 4500, 2200, 3800] 
colors = ['#2ca02c', '#ff7f0e', '#1f77b4', '#17becf']

# 2. Latency Data (ms) vs Concurrency Levels
concurrency_levels = [1, 10, 50, 100]
lat_tinydb = [2, 45, 150, 500] 
lat_mysql = [5, 8, 12, 18]
lat_odeta_sync = [0.5, 5, 25, 80]     # Blocks main thread
lat_odeta_async = [0.8, 2, 8, 25]     # Non-blocking, better queuing

# 3. Radar Chart Data (Scores 1-5)
radar_categories = ['Setup Ease', 'Read Speed', 'Write Concurrency', 'Durability', 'Flexibility']
radar_data = {
    'TinyDB': [5, 2, 1, 2, 5],
    'MySQL': [2, 4, 5, 5, 2],
    'ODETA': [5, 5, 3, 5, 5]
}

# ==========================================
# PLOTTING FUNCTIONS
# ==========================================

def plot_throughput():
    plt.figure(figsize=(10, 6))
    bars = plt.bar(technologies, throughput_ops, color=colors, alpha=0.85, width=0.6)
    
    # Add data labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 50,
                 f'{int(height)}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.title('Throughput Comparison (Requests/Sec)\n(Higher is Better)', fontsize=16)
    plt.ylabel('Operations / Second', fontsize=14)
    plt.ylim(0, 5000)
    plt.tight_layout()
    plt.savefig('throughput_chart.png', dpi=300)
    print("Generated: throughput_chart.png")

def plot_latency():
    plt.figure(figsize=(10, 6))
    
    # Plot lines
    plt.plot(concurrency_levels, lat_tinydb, marker='o', label='TinyDB', color='#2ca02c', linestyle='--')
    plt.plot(concurrency_levels, lat_mysql, marker='s', label='MySQL', color='#ff7f0e', linewidth=2)
    plt.plot(concurrency_levels, lat_odeta_sync, marker='^', label='ODETA (Sync)', color='#1f77b4', linewidth=2)
    plt.plot(concurrency_levels, lat_odeta_async, marker='*', label='ODETA (Async)', color='#17becf', linewidth=3, markersize=10)

    plt.title('P95 Latency vs Load\n(Lower is Better)', fontsize=16)
    plt.xlabel('Concurrent Users', fontsize=14)
    plt.ylabel('Latency (ms) - Log Scale', fontsize=14)
    plt.yscale('log') # Log scale handles the huge range differences
    
    plt.legend(fontsize=12)
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.tight_layout()
    plt.savefig('latency_chart.png', dpi=300)
    print("Generated: latency_chart.png")

def plot_radar():
    # Setup angles
    num_vars = len(radar_categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1] # Close the loop for the shape

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    # Draw one axe per variable + labels
    plt.xticks(angles[:-1], radar_categories, fontsize=12)
    
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=10)
    plt.ylim(0, 5.5)
    
    # Plot each
    colors_radar = ['#2ca02c', '#ff7f0e', '#1f77b4']
    for idx, (name, values) in enumerate(radar_data.items()):
        values += values[:1] # Close the loop
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=name, color=colors_radar[idx])
        ax.fill(angles, values, color=colors_radar[idx], alpha=0.1)
    
    plt.title('Architecture Trade-off Analysis', size=20, y=1.05)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12)
    plt.tight_layout()
    plt.savefig('radar_chart.png', dpi=300)
    print("Generated: radar_chart.png")

# ==========================================
# EXECUTE
# ==========================================
if __name__ == "__main__":
    plot_throughput()
    plot_latency()
    plot_radar()