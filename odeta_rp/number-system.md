# Digital Electronics: Complete Study Textbook

## A Comprehensive Guide to Digital Electronics and Logic Design

**Version 1.0**  
**Author:** Compiled from Lecture Series  
**Date:** November 2025

---

## Table of Contents

1. Introduction & Number Systems (Lectures 1–3)
2. Number Representation (Lectures 4–5)
3. Boolean Algebra (Lecture 6)
4. Boolean Expressions & Simplification (Lecture 7)
5. Karnaugh Maps (K-Map) - Fundamentals & Reduction (Lectures 8–11)
6. Combinational Circuits (Lectures 12–15)
7. Sequential Circuits (Lectures 16–18)
8. Code Conversion & Binary Arithmetic (Lecture 19)
9. Doubt Session & Exam Strategy (Lecture 20)

---

# Chapter 1: Fundamentals of Number Systems

## 1.1 What is a Number System?

A **number system** is a systematic method of representing numerical values using a specific set of symbols or digits. Every number system has two key properties:

1. **Base (or Radix):** The total count of unique symbols/digits available
2. **Digits/Symbols:** The individual characters used to construct numbers

For any number system with base B:
- **Available digits range from:** 0 to (B−1)
- **Total unique digits:** B

### Common Number Systems

| System | Base | Digits | Example |
|--------|------|--------|---------|
| Binary | 2 | 0, 1 | $1010_2$ |
| Octal | 8 | 0–7 | $312_8$ |
| Decimal | 10 | 0–9 | $127_{10}$ |
| Hexadecimal | 16 | 0–9, A–F | $\text{A5F}_{16}$ |

## 1.2 Why Different Number Systems?

- **Binary:** Direct match with digital circuit states (ON/OFF, 1/0). All computer data ultimately represented in binary.
- **Octal:** 3 binary bits = 1 octal digit ($2^3 = 8$). More compact than binary for human readability.
- **Hexadecimal:** 4 binary bits = 1 hex digit ($2^4 = 16$). Used for memory addresses, color codes, machine instructions.
- **Decimal:** Familiar to humans for everyday calculations.

## 1.3 Bits, Bytes, and Memory Units

Understanding data storage units is essential for digital electronics:

| Unit | Definition | Equivalent |
|------|-----------|------------|
| **Bit** | Single binary digit (0 or 1) | $2^0 = 1$ value |
| **Nibble** | 4 bits | 1 hexadecimal digit |
| **Byte** | 8 bits | $2^8 = 256$ possible values |
| **Kilobyte (KB)** | 1024 bytes | $2^{10}$ bytes |
| **Megabyte (MB)** | 1024 KB | $2^{20}$ bytes |
| **Gigabyte (GB)** | 1024 MB | $2^{30}$ bytes |
| **Terabyte (TB)** | 1024 GB | $2^{40}$ bytes |

## 1.4 Essential Powers of 2

Memorize these—they appear constantly in exams:

| Power | Value | Power | Value |
|-------|-------|-------|-------|
| $2^0$ | 1 | $2^8$ | 256 |
| $2^1$ | 2 | $2^9$ | 512 |
| $2^2$ | 4 | $2^{10}$ | 1024 |
| $2^3$ | 8 | $2^{12}$ | 4096 |
| $2^4$ | 16 | $2^{16}$ | 65536 |
| $2^5$ | 32 | $2^{20}$ | 1048576 |
| $2^6$ | 64 | $2^{24}$ | 16777216 |
| $2^7$ | 128 | $2^{32}$ | 4294967296 |

---

# Chapter 2: Number System Conversions

## 2.1 Three Main Conversion Types

### **Type 1: Any Base → Decimal**

**Method:** Multiply each digit by its base raised to the power of its positional value, then sum.

$$N_B = d_n \cdot B^n + d_{n-1} \cdot B^{n-1} + \cdots + d_1 \cdot B^1 + d_0 \cdot B^0$$

**Example:** Convert $1010_2$ to decimal

$$1010_2 = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0 = 8 + 0 + 2 + 0 = 10_{10}$$

### **Type 2: Decimal → Any Base**

**Integer Part:** Successive division by target base. Record remainders; read from bottom to top.

**Fractional Part:** Successive multiplication by target base. Record integer parts; repeat until desired precision.

**Example:** Convert $25_{10}$ to binary

\begin{table}
\begin{tabular}{|c|c|c|}
\hline
Division & Quotient & Remainder \\
\hline
25 ÷ 2 & 12 & 1 \\
12 ÷ 2 & 6 & 0 \\
6 ÷ 2 & 3 & 0 \\
3 ÷ 2 & 1 & 1 \\
1 ÷ 2 & 0 & 1 \\
\hline
\end{tabular}
\end{table}

Read remainders bottom to top: **$11001_2$**

### **Type 3: Non-Decimal Base → Non-Decimal Base**

**Method 1 (General):** Convert via decimal
- Source base → decimal → target base

**Method 2 (For power-of-2 bases):** Direct bit grouping
- Binary to Octal: Group 3 bits (since $2^3 = 8$)
- Binary to Hexadecimal: Group 4 bits (since $2^4 = 16$)

**Example:** Convert $11010111_2$ to hexadecimal

Group into 4-bit chunks: $1101 \: 0111$

$1101_2 = 13 = \text{D}_{16}$; $0111_2 = 7_{16}$

**Answer:** $\text{D7}_{16}$

## 2.2 Worked Examples

**Example 1:** Binary to Decimal
- Convert $11011_2$
- $11011_2 = 1(16) + 1(8) + 0(4) + 1(2) + 1(1) = 27_{10}$

**Example 2:** Octal to Decimal
- Convert $312_8$
- $312_8 = 3(64) + 1(8) + 2(1) = 202_{10}$

**Example 3:** Hexadecimal to Decimal
- Convert $\text{A5F}_{16}$
- $\text{A5F}_{16} = 10(256) + 5(16) + 15(1) = 2655_{10}$

---

# Chapter 3: Number Representation in Binary

## 3.1 Signed Numbers: Three Representations

Digital systems must represent both positive and negative numbers. Three methods exist:

### **Sign-Magnitude Representation**

**Structure:** Most Significant Bit (MSB) = sign bit (0 for +, 1 for −); remaining bits = magnitude

**For Positive Numbers:**
- First bit: 0
- Remaining bits: Binary representation of magnitude

**For Negative Numbers:**
- First bit: 1
- Remaining bits: Binary representation of magnitude (same as positive counterpart)

**Example:** Represent +10 and −10 in 4-bit sign-magnitude
- +10 = $0 \: 1010$ (0 for positive, 1010 is 10 in binary)
- −10 = $1 \: 1010$ (1 for negative, 1010 is magnitude)

**Range (for n-bit):**
- Smallest: $-(2^{n-1} - 1)$
- Largest: $+(2^{n-1} - 1)$
- **Problem:** Zero has two representations: $0 \: 0000$ and $1 \: 0000$

### **One's Complement Representation**

**For Positive Numbers:** Same as sign-magnitude (MSB = 0, rest = magnitude)

**For Negative Numbers:** Flip all bits of the positive number's binary representation

**Process:**
1. Write positive number in binary
2. Flip every bit: 0→1, 1→0
3. Result is one's complement of negative number

**Example:** Represent +10 and −10 in 8-bit one's complement
- +10 = $00001010$
- −10: Flip all bits of $00001010$ → $11110101$

**Range (for n-bit):**
- Smallest: $-(2^{n-1} - 1)$
- Largest: $+(2^{n-1} - 1)$
- **Problem:** Zero still has two representations

### **Two's Complement Representation (Most Important)**

**For Positive Numbers:** MSB = 0, rest = magnitude (same as sign-magnitude)

**For Negative Numbers:** 
1. Write one's complement
2. Add 1 to the result

**Process for −n:**
1. Find binary of positive n
2. Flip all bits (one's complement)
3. Add 1

**Example:** Represent +10 and −10 in 8-bit two's complement
- +10 = $00001010$
- One's complement: $11110101$
- Add 1: $11110110$
- −10 = $11110110$

**Range (for n-bit):**
- Smallest: $-2^{n-1}$
- Largest: $+(2^{n-1} - 1)$
- **Advantage:** Only ONE representation for zero ($00000000$)

## 3.2 Comparison Table

\begin{table}
\centering
\begin{tabular}{|l|c|c|c|}
\hline
\textbf{Aspect} & \textbf{Sign-Magnitude} & \textbf{One's Complement} & \textbf{Two's Complement} \\
\hline
Positive representation & Standard binary & Standard binary & Standard binary \\
Negative representation & Flip MSB only & Flip all bits & Flip + add 1 \\
Zero representations & 2 & 2 & 1 \\
Range (8-bit) & −127 to +127 & −127 to +127 & −128 to +127 \\
Arithmetic efficiency & Low & Medium & High \\
Used in computers & No & Rarely & Yes \\
\hline
\end{tabular}
\caption{Comparison of Number Representations}
\end{table}

## 3.3 Direct Method for Two's Complement

**To directly convert decimal to two's complement:**

For a given negative number like −21 in 8-bit:

1. Find the smallest $2^n \geq |$number$|$
2. Calculate: $2^n - |$number$|$
3. Convert result to binary

**Example:** −21 in 8-bit
- $2^8 = 256$
- $256 − 21 = 235$
- $235 = 128 + 64 + 32 + 8 + 2 + 1 = 11101011_2$

**Verification:** Read directly: $1 \cdot 128 + 1 \cdot 64 + 1 \cdot 32 + 0 \cdot 16 + 1 \cdot 8 + 0 \cdot 4 + 1 \cdot 2 + 1 \cdot 1 = 235$, meaning −21. ✓

## 3.4 Arithmetic in Two's Complement

Two's complement is preferred because:
- Arithmetic operations (addition, subtraction) work naturally
- No special handling needed; ignore carry-out
- Most efficient for digital circuits

**Example:** Add +10 and −10 using 8-bit two's complement
- +10 = $00001010$
- −10 = $11110110$
- Sum = $00000000$ (ignore overflow carry)
- Result: 0 ✓

---

# Chapter 4: Boolean Algebra & Logic Gates

## 4.1 Fundamental Logic Gates

Digital logic is built on gates that perform Boolean operations. Each gate implements a specific Boolean function.

### **1. AND Gate**

**Symbol:** 
- Output = 1 only when ALL inputs are 1
- Otherwise, output = 0

**Truth Table (2-input):**

| A | B | Y = A·B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Boolean Expression:** $Y = A \cdot B$ (or just AB)

### **2. OR Gate**

**Symbol:** 
- Output = 1 when at least ONE input is 1
- Output = 0 only when ALL inputs are 0

**Truth Table (2-input):**

| A | B | Y = A+B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**Boolean Expression:** $Y = A + B$

### **3. NOT Gate (Inverter)**

**Symbol:** 
- Output is opposite of input
- Input 0 → Output 1
- Input 1 → Output 0

**Truth Table:**

| A | $\bar{A}$ |
|---|----------|
| 0 | 1 |
| 1 | 0 |

**Boolean Expression:** $Y = \bar{A}$ (or A')

### **4. NAND Gate**

**Definition:** AND gate followed by NOT (negated AND)

**Truth Table (2-input):**

| A | B | Y = $\overline{A \cdot B}$ |
|---|---|----------------------|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Key Property:** NAND is a universal gate—all other gates can be constructed from NAND gates.

### **5. NOR Gate**

**Definition:** OR gate followed by NOT (negated OR)

**Truth Table (2-input):**

| A | B | Y = $\overline{A + B}$ |
|---|---|----------------------|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

**Key Property:** NOR is also a universal gate.

### **6. XOR Gate (Exclusive OR)**

**Definition:** Output = 1 when inputs are different; 0 when inputs are same

**Truth Table (2-input):**

| A | B | Y = A ⊕ B |
|---|---|-----------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Boolean Expression:** $Y = A \bar{B} + \bar{A} B$

**Application:** Used in comparators, parity checkers, adders

### **7. XNOR Gate (Exclusive NOR)**

**Definition:** Negated XOR; output = 1 when inputs are same

**Truth Table (2-input):**

| A | B | Y = A ⊙ B |
|---|---|-----------|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## 4.2 Boolean Algebra Laws and Theorems

Boolean algebra simplifies logic expressions. Key laws include:

### **Basic Laws**

\begin{itemize}
\item **Commutative Law:** $A + B = B + A$ and $A \cdot B = B \cdot A$
\item **Associative Law:** $(A + B) + C = A + (B + C)$ and $(A \cdot B) \cdot C = A \cdot (B \cdot C)$
\item **Distributive Law:** $A(B + C) = AB + AC$ and $A + BC = (A + B)(A + C)$
\end{itemize}

### **Absorption and Redundance**

\begin{itemize}
\item **Absorption:** $A + AB = A$ and $A(A + B) = A$
\item **Redundance:** $A + \bar{A}B = A + B$
\end{itemize}

### **DeMorgan's Theorem (Critical for Exams)**

These theorems help convert between AND/OR and NAND/NOR:

$$\overline{A + B} = \bar{A} \cdot \bar{B}$$ (NOR is NAND of inverted inputs)

$$\overline{A \cdot B} = \bar{A} + \bar{B}$$ (NAND is NOR of inverted inputs)

**General form (n variables):**

$$\overline{A_1 + A_2 + \cdots + A_n} = \bar{A_1} \cdot \bar{A_2} \cdot \cdots \cdot \bar{A_n}$$

$$\overline{A_1 \cdot A_2 \cdot \cdots \cdot A_n} = \bar{A_1} + \bar{A_2} + \cdots + \bar{A_n}$$

### **Complement Laws**

\begin{itemize}
\item $A + \bar{A} = 1$ (Always true)
\item $A \cdot \bar{A} = 0$ (Always false)
\item $\bar{\bar{A}} = A$ (Double negation = original)
\end{itemize}

### **Identity Laws**

\begin{itemize}
\item $A + 0 = A$ and $A \cdot 1 = A$
\item $A + 1 = 1$ and $A \cdot 0 = 0$
\end{itemize}

---

# Chapter 5: Boolean Expressions & Simplification

## 5.1 Standard Forms

Boolean expressions can be written in two standard forms:

### **Sum of Products (SOP)**

Expression is a sum (OR) of products (AND terms):

$$Y = AB + AC + BC$$

- Each product term called a **minterm**
- Implementation: AND gates → OR gate

### **Product of Sums (POS)**

Expression is a product (AND) of sum (OR terms):

$$Y = (A + B)(A + C)(B + C)$$

- Each sum term called a **maxterm**
- Implementation: OR gates → AND gate

## 5.2 Simplification Techniques

### **Algebraic Simplification**

Using Boolean laws to reduce expressions:

**Example:**
$$Y = AB + A\bar{B} + \bar{A}\bar{B}$$
$$= A(B + \bar{B}) + \bar{A}\bar{B}$$
$$= A(1) + \bar{A}\bar{B}$$ (since $B + \bar{B} = 1$)
$$= A + \bar{A}\bar{B}$$

### **From Truth Table to Expression**

1. List rows where output = 1
2. Write minterm for each (AND inputs that give 1)
3. OR all minterms

**Example Truth Table:**

| A | B | C | Y |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

Rows with Y = 1: 1, 3, 5, 6, 7

Minterms:
- Row 1: $\bar{A}\bar{B}C$
- Row 3: $\bar{A}BC$
- Row 5: $A\bar{B}C$
- Row 6: $AB\bar{C}$
- Row 7: $ABC$

Expression: $Y = \bar{A}\bar{B}C + \bar{A}BC + A\bar{B}C + AB\bar{C} + ABC$

---

# Chapter 6: Karnaugh Maps (K-Map)

## 6.1 What is a Karnaugh Map?

A **Karnaugh Map (K-Map)** is a graphical method for simplifying Boolean expressions. It's especially useful for expressions with 2–6 variables.

**Advantages:**
- Visual representation makes grouping obvious
- Faster than algebraic simplification
- Minimizes errors
- Produces minimal expressions with fewest gates

## 6.2 Structure of K-Maps

K-Maps arrange truth table values in a grid where adjacent cells differ by only one variable.

### **2-Variable K-Map**

\begin{table}
\centering
\begin{tabular}{c|c|c|}
\cline{2-3}
& $\bar{B}$ & $B$ \\
\hline
$\bar{A}$ & 0 & 1 \\
\hline
$A$ & 2 & 3 \\
\hline
\end{tabular}
\caption{2-Variable K-Map: cell values (minterms)}
\end{table}

### **3-Variable K-Map**

\begin{table}
\centering
\begin{tabular}{c|c|c|c|c|}
\cline{2-5}
& $\bar{B}\bar{C}$ & $\bar{B}C$ & $BC$ & $B\bar{C}$ \\
\hline
$\bar{A}$ & 0 & 1 & 3 & 2 \\
\hline
$A$ & 4 & 5 & 7 & 6 \\
\hline
\end{tabular}
\caption{3-Variable K-Map}
\end{table}

### **4-Variable K-Map**

\begin{table}
\centering
\begin{tabular}{c|c|c|c|c|}
\cline{2-5}
& $\bar{C}\bar{D}$ & $\bar{C}D$ & $CD$ & $C\bar{D}$ \\
\hline
$\bar{A}\bar{B}$ & 0 & 1 & 3 & 2 \\
\hline
$\bar{A}B$ & 4 & 5 & 7 & 6 \\
\hline
$AB$ & 12 & 13 & 15 & 14 \\
\hline
$A\bar{B}$ & 8 & 9 & 11 & 10 \\
\hline
\end{tabular}
\caption{4-Variable K-Map}
\end{table}

## 6.3 Grouping Rules for Minimization

**Valid group sizes:** 1, 2, 4, 8, 16, ... (powers of 2 only)

**Grouping principles:**
1. Larger groups are better (eliminate more variables)
2. Each cell with 1 must be included in at least one group
3. Groups can overlap
4. Groups wrap around edges (top-bottom, left-right)
5. Avoid single isolated 1s (group with neighbors if possible)

**Number of variables eliminated:** If group has $2^n$ cells, n variables are eliminated

**Examples:**
- Group of 2 cells → eliminates 1 variable
- Group of 4 cells → eliminates 2 variables
- Group of 8 cells → eliminates 3 variables

## 6.4 Worked Example: 3-Variable Simplification

**Problem:** Simplify $Y = \bar{A}\bar{B}C + \bar{A}BC + AB\bar{C} + ABC$

**Step 1:** Identify minterms: 1, 3, 6, 7

**Step 2:** Place 1s in K-Map at positions 1, 3, 6, 7

\begin{table}
\centering
\begin{tabular}{c|c|c|c|c|}
\cline{2-5}
& $\bar{B}\bar{C}$ & $\bar{B}C$ & $BC$ & $B\bar{C}$ \\
\hline
$\bar{A}$ & 0 & 1 & 1 & 0 \\
\hline
$A$ & 0 & 0 & 1 & 1 \\
\hline
\end{tabular}
\caption{K-Map with 1s placed}
\end{table}

**Step 3:** Group adjacent 1s
- Group 1: Cells 1, 3 (vertical pair in column $\bar{B}C$ and $BC$) → eliminates B → $\bar{A}C$
- Group 2: Cells 6, 7 (horizontal pair in row A) → eliminates B → $AC$

**Step 4:** Write simplified expression:
$$Y = \bar{A}C + AC = C(\bar{A} + A) = C$$

**Result:** The simplified expression is just $Y = C$

---

# Chapter 7: Combinational Circuits

## 7.1 What are Combinational Circuits?

**Definition:** Digital circuits where output depends ONLY on current inputs, not on any previous state (no memory).

**Key Characteristics:**
- No memory elements (no flip-flops, no latches)
- Output immediately changes when input changes
- No internal state or history

**General Structure:**

\begin{figure}
\centering
\includegraphics[width=0.6\textwidth]{combinational}
\caption{General combinational circuit structure}
\end{figure}

Inputs → Combinational Circuit (Logic Gates) → Outputs

## 7.2 Common Combinational Building Blocks

### **1. Adders**

#### **Half Adder**
- Adds two 1-bit numbers
- Produces sum and carry

**Truth Table:**

| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

**Boolean Expressions:**
- $\text{Sum} = A \oplus B$
- $\text{Carry} = A \cdot B$

#### **Full Adder**
- Adds three 1-bit numbers (A, B, and Carry-in)
- Produces sum and carry-out

**Boolean Expressions:**
- $\text{Sum} = A \oplus B \oplus C_{in}$
- $C_{out} = AB + (A \oplus B) C_{in}$

### **2. Encoders**

**Purpose:** Converts one active input line to binary code

**Example: 4-to-2 Encoder**
- 4 input lines, 2 output lines
- Only one input should be high (1)
- Output shows binary index of active input

| I₀ | I₁ | I₂ | I₃ | Y₁ | Y₀ |
|----|----|----|----|----|-----|
| 1 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 1 | 0 |
| 0 | 0 | 0 | 1 | 1 | 1 |

### **3. Decoders**

**Purpose:** Converts binary input code to one active output line

**Example: 2-to-4 Decoder**
- 2 input lines, 4 output lines
- Exactly one output line is 1 based on input

| A | B | Y₀ | Y₁ | Y₂ | Y₃ |
|---|---|----|----|----|----|
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 |

### **4. Multiplexers (MUX)**

**Purpose:** Selects one of multiple input lines and routes it to output based on select lines

**Example: 4-to-1 Multiplexer**
- 4 data inputs, 1 output
- 2 select lines choose which input appears at output

**Boolean Expression:**
$$Y = \bar{S_1}\bar{S_0}I_0 + \bar{S_1}S_0I_1 + S_1\bar{S_0}I_2 + S_1S_0I_3$$

### **5. Demultiplexers (DEMUX)**

**Purpose:** Routes single input to one of multiple output lines based on select lines

**Example: 1-to-4 Demultiplexer**
- 1 data input, 4 outputs
- Input appears on output selected by 2 select lines

## 7.3 Design Process

**Step 1:** Understand the problem and create truth table

**Step 2:** Write Boolean expressions from truth table

**Step 3:** Simplify using Boolean algebra or K-Maps

**Step 4:** Draw logic circuit (gates and connections)

**Step 5:** Verify circuit behavior matches requirements

---

# Chapter 8: Sequential Circuits

## 8.1 Introduction to Sequential Circuits

**Definition:** Circuits where output depends on BOTH current inputs AND previous state (have memory)

**Key Differences from Combinational:**

| Aspect | Combinational | Sequential |
|--------|-------------|-----------|
| Memory | No | Yes |
| Output depends on | Current inputs only | Current input + previous state |
| Storage elements | None | Latches, flip-flops |
| Time factor | Irrelevant | Critical |
| Complexity | Lower | Higher |

## 8.2 Basic Storage Elements

### **SR Latch (Set-Reset)**

**Purpose:** Simplest sequential element; can store 1 bit

**Using NAND gates:**

\begin{figure}
\centering
\caption{SR Latch using NAND gates}
\end{figure}

**Behavior:**
- **S = 0, R = 1:** Set (Q = 1)
- **S = 1, R = 0:** Reset (Q = 0)
- **S = 1, R = 1:** Hold (Q maintains previous state)
- **S = 0, R = 0:** Invalid (forbidden; Q and Q' both become 1)

### **D Latch (Data Latch)**

**Purpose:** Stores data based on enable signal (not clock)

**Characteristic Equation:** When enabled, Q follows D input

**Application:** Temporary data storage, multiplexing

### **SR Flip-Flop (Clocked)**

**Difference from Latch:** Changes state only on clock edge (edge-triggered), not continuously

**Master-Slave Configuration:** Two latches; master follows input when clock is high, slave copies master when clock goes low

**Advantage:** Eliminates race conditions and unpredictable behavior

## 8.3 Types of Flip-Flops

### **1. SR Flip-Flop (Set-Reset)**

**Behavior:** Same as SR latch but edge-triggered

**Truth Table (on clock edge):**

| S | R | Next State |
|---|---|-----------|
| 0 | 0 | No change (hold) |
| 0 | 1 | Reset (Q ← 0) |
| 1 | 0 | Set (Q ← 1) |
| 1 | 1 | Invalid |

### **2. D Flip-Flop (Data)**

**Purpose:** Captures input D on clock edge

**Characteristic:** Q follows D on active clock edge

**Truth Table:**

| D | Next Q |
|---|--------|
| 0 | 0 |
| 1 | 1 |

**Application:** Data transfer, delay elements, registers

### **3. JK Flip-Flop (Jack-Kilby)**

**Purpose:** Universal flip-flop; most flexible

**Characteristic:** 
- J = Set input, K = Reset input
- When J = K = 1, flip-flop toggles (Q ← Q')

**Truth Table:**

| J | K | Next State |
|---|---|-----------|
| 0 | 0 | No change |
| 0 | 1 | Reset (Q ← 0) |
| 1 | 0 | Set (Q ← 1) |
| 1 | 1 | Toggle (Q ← Q') |

### **4. T Flip-Flop (Toggle)**

**Purpose:** Toggles state or holds

**Characteristic:**
- T = 0: Hold current state
- T = 1: Toggle (Q ← Q')

**Truth Table:**

| T | Next State |
|---|-----------|
| 0 | No change |
| 1 | Toggle |

**Application:** Counters, frequency dividers

## 8.4 State Diagrams and Tables

**State Diagram:** Circle nodes represent states; arrows show transitions based on inputs

**State Table:** Rows = current state + input; columns = next state + output

**Example: 2-bit counter state diagram using T flip-flops**

States: 00 → 01 → 10 → 11 → 00 (repeating)

---

# Chapter 9: Code Conversion & Binary Arithmetic

## 9.1 Code Conversions

### **Binary to BCD (Binary Coded Decimal)**

**Method:** 
1. Convert binary to decimal
2. Convert each decimal digit to 4-bit binary (BCD)

**Example:** Convert $11001_2$ to BCD
- $11001_2 = 25_{10}$
- Decimal 2 = $0010_2$ (BCD)
- Decimal 5 = $0101_2$ (BCD)
- Result: $0010 \: 0101$ (BCD)

### **BCD to Binary**

**Method:**
1. Convert each BCD group to decimal digit
2. Assemble decimal number
3. Convert decimal to binary

**Example:** Convert $0100 \: 1001 \: 0111$ (BCD) to binary
- 0100 = 4, 1001 = 9, 0111 = 7
- Decimal: 497
- Binary: $111110001_2$

### **Binary to Gray Code**

**Method:** 
- MSB of Gray = MSB of Binary
- Each subsequent Gray bit = XOR of binary bit and previous binary bit

$$G_i = B_i \oplus B_{i+1}$$

**Example:** Convert $1011_2$ to Gray
- $G_3 = B_3 = 1$
- $G_2 = B_3 \oplus B_2 = 1 \oplus 0 = 1$
- $G_1 = B_2 \oplus B_1 = 0 \oplus 1 = 1$
- $G_0 = B_1 \oplus B_0 = 1 \oplus 1 = 0$
- Result: $1110_{\text{Gray}}$

### **Gray Code to Binary**

**Method:**
- MSB of Binary = MSB of Gray
- Each subsequent Binary bit = XOR of Gray bit with previous Binary bit

$$B_i = G_i \oplus B_{i+1}$$

## 9.2 Binary Arithmetic

### **Binary Addition**

**Rules:**
- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 10 (0 with carry 1)
- 1 + 1 + 1 = 11 (1 with carry 1)

**Example:** Add $1101_2 + 1011_2$

  1101
+  1011
------
  11000

Result: $11000_2 = 24_{10}$ (Verify: 13 + 11 = 24 ✓)

### **Binary Subtraction**

**Method 1:** Direct subtraction (borrow method)

**Method 2:** Two's complement addition (preferred in computers)
1. Take two's complement of subtrahend
2. Add to minuend
3. Ignore final carry

**Example:** $1101_2 - 1011_2 = ?$

Using two's complement:
- Two's complement of $1011_2$ = $0101_2$
- $1101 + 0101 = 10010$
- Ignore carry: Result = $0010_2 = 2_{10}$ (Verify: 13 − 11 = 2 ✓)

### **Binary Multiplication**

**Method:** Similar to decimal multiplication; partial products

**Example:** $1101_2 \times 11_2$

     1101
   ×   11
   ------
     1101  (1101 × 1)
    1101   (1101 × 1, shifted)
   ------
   100111

Result: $100111_2 = 39_{10}$ (Verify: 13 × 3 = 39 ✓)

### **Binary Division**

**Method:** Long division (similar to decimal)

**Example:** $1100_2 ÷ 11_2$

Divide until quotient found, remainder shows fractional part if any.

---

# Chapter 10: Exam Strategy and Doubt Clarification

## 10.1 Common Question Types

### **Type 1: Direct Conversion**
"Convert $1010_2$ to decimal" → Apply positional notation method

### **Type 2: Number Representation**
"Represent −10 in 8-bit two's complement" → Flip bits and add 1

### **Type 3: Boolean Simplification**
"Simplify $AB + A\bar{B}$" → Use Boolean algebra or K-Map

### **Type 4: Combinational Circuit Design**
"Design a circuit for the given truth table" → Write expression → Simplify → Draw circuit

### **Type 5: Sequential Circuit Analysis**
"Given flip-flop inputs, find next state" → Use characteristic equations

## 10.2 Tips for Success

1. **Memorize Powers of 2:** Essential reference for all conversions
2. **Master Two's Complement:** Most important representation; used in all computers
3. **Practice K-Maps:** Faster than algebraic simplification; reduces errors
4. **Verify Answers:** Convert back to original base to check correctness
5. **Draw Diagrams:** Visual representation helps understanding and catches errors
6. **Practice Problems:** Consistent practice is key to mastery

## 10.3 Frequently Asked Doubts

**Q1:** Why do we use two's complement instead of one's complement?

**A:** Two's complement has advantages:
- Single representation for zero
- Natural arithmetic (addition works without special handling)
- Efficient hardware implementation
- Industry standard

**Q2:** How do I know the range of numbers in n-bit representation?

**A:** 
- Unsigned: 0 to $2^n - 1$
- Sign-magnitude: $-(2^{n-1} - 1)$ to $+(2^{n-1} - 1)$
- One's complement: $-(2^{n-1} - 1)$ to $+(2^{n-1} - 1)$
- Two's complement: $-2^{n-1}$ to $+(2^{n-1} - 1)$

**Q3:** When should I use K-Maps vs. algebraic simplification?

**A:** 
- K-Map: Fast, visual, fewer errors; best for 2–6 variables
- Algebraic: Good for understanding; sometimes required in exams
- Practice both methods

**Q4:** What's the difference between latches and flip-flops?

**A:**
- **Latches:** Level-triggered; respond to input as long as enable is active
- **Flip-flops:** Edge-triggered; respond only at clock edge; more predictable behavior

## 10.4 Key Formulas Reference

**Powers of 2:** $2^0 = 1, 2^1 = 2, 2^2 = 4, ..., 2^{10} = 1024$

**Conversion (Base B to Decimal):**
$$N_{10} = d_n B^n + d_{n-1} B^{n-1} + \cdots + d_0 B^0$$

**Two's Complement Range (n-bit signed):**
- Minimum: $-2^{n-1}$
- Maximum: $+2^{n-1} - 1$

**K-Map Grouping:** Groups of size $2^k$ eliminate $k$ variables

**Boolean Laws:**
- DeMorgan: $\overline{A+B} = \bar{A} \cdot \bar{B}$ and $\overline{A \cdot B} = \bar{A} + \bar{B}$
- Absorption: $A + AB = A$ and $A(A+B) = A$

---

# Appendix A: Quick Reference Tables

## Memory Units

| Unit | Size | Equivalent |
|------|------|-----------|
| Kilobyte (KB) | 1024 bytes | $2^{10}$ bytes |
| Megabyte (MB) | 1024 KB | $2^{20}$ bytes |
| Gigabyte (GB) | 1024 MB | $2^{30}$ bytes |
| Terabyte (TB) | 1024 GB | $2^{40}$ bytes |

## Logic Gate Summary

| Gate | Input | Output | Use |
|------|-------|--------|-----|
| AND | All 1 | 1 | All conditions must be true |
| OR | Any 1 | 1 | At least one condition true |
| NOT | - | Opposite | Invert signal |
| NAND | All 1 | 0 | Universal gate |
| NOR | Any 0 | 1 | Universal gate |
| XOR | Different | 1 | Difference detection |
| XNOR | Same | 1 | Equality check |

## Boolean Laws Quick Ref

| Law | Form | Application |
|-----|------|------------|
| Commutative | A + B = B + A | Order doesn't matter |
| Associative | (A+B)+C = A+(B+C) | Grouping doesn't matter |
| Distributive | A(B+C) = AB+AC | Factor out common terms |
| Absorption | A + AB = A | Eliminate redundant terms |
| DeMorgan | $\overline{A+B} = \bar{A}\bar{B}$ | Convert AND/OR |

---

# Appendix B: Practice Problems

### **Problem Set 1: Number System Conversions**

1. Convert $11011_2$ to decimal
2. Convert $25_{10}$ to binary
3. Convert $312_8$ to decimal
4. Convert $\text{A5F}_{16}$ to decimal
5. Convert $110101_2$ to hexadecimal

### **Problem Set 2: Number Representation**

1. Represent +15 and −15 in 8-bit sign-magnitude
2. Represent +15 and −15 in 8-bit one's complement
3. Represent +15 and −15 in 8-bit two's complement
4. What is the range of 5-bit unsigned numbers?
5. What is the range of 5-bit signed (two's complement) numbers?

### **Problem Set 3: Boolean Algebra**

1. Simplify $\overline{A+B} \cdot C$
2. Simplify $AB + A\bar{B} + \bar{A}B$
3. Apply DeMorgan's theorem to $\overline{A \cdot B \cdot C}$
4. Construct truth table for $Y = AB + \bar{A}\bar{B}$
5. Draw logic circuit for $Y = (A+B)(A+C)$

### **Problem Set 4: K-Map Simplification**

1. Simplify using K-Map: $\bar{A}\bar{B} + \bar{A}B + AB$
2. Simplify using K-Map: $\bar{A}\bar{B}\bar{C} + \bar{A}B\bar{C} + AB\bar{C} + ABC$
3. Minimize the following 4-variable function using K-Map:
   $\bar{A}\bar{B}\bar{C}\bar{D} + \bar{A}\bar{B}\bar{C}D + \bar{A}B\bar{C}\bar{D} + AB\bar{C}\bar{D}$

### **Problem Set 5: Binary Arithmetic**

1. Add $1101_2 + 1011_2$
2. Subtract $1101_2 - 1011_2$ using two's complement
3. Multiply $1101_2 \times 11_2$
4. Convert $100111_2$ to BCD
5. Convert $0101 \: 1001_{\text{BCD}}$ to binary

---

# Conclusion

This textbook provides comprehensive coverage of Digital Electronics from fundamentals through sequential circuits. Key success factors:

1. **Solid Foundation:** Master number systems and conversions
2. **Boolean Algebra:** Understand logic laws and their applications
3. **Practical Skills:** Learn K-Maps and circuit design
4. **Consistency:** Regular practice on all topics
5. **Verification:** Always check answers through alternate methods

Digital Electronics is the gateway to understanding computer architecture, microprocessors, and advanced computing systems. With mastery of these concepts, students are well-prepared for:

- Competitive examinations (SSC, NET, GATE)
- Engineering degree programs
- Embedded systems and microcontroller design
- Professional careers in electronics and computing

---

## References

- Lecture Series: Digital Electronics (Lectures 1–20)
- Standard references: Boolean algebra, logic design
- Examination patterns: SSC, NET, GATE, and other competitive exams

---

**Study Tips:**
- Review key formulas and theorems regularly
- Practice converting between number systems daily
- Work through additional practice problems beyond those provided
- Form study groups to discuss complex concepts
- Use diagrams and visual aids for better understanding

**Best of luck with your Digital Electronics journey!**

---

*Last Updated: November 2025*