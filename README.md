# Week 1 — Python Fundamentals + NumPy + Linear Algebra

Part of a self-designed 16-week study plan (June–October 2026) covering
Python, scientific computing, and applied mathematics, ahead of a
Computational Mathematics Master's program.

**Goal this week:** revise core Python, start NumPy, and relearn linear
algebra concepts (vectors, matrices, eigenvalues, Ax=b) by implementing
them in code rather than just reading theory.

## Contents

### Python fundamentals
- `lists_loops_functions.py` — list operations, loops, and functions
  written without relying on Python built-ins (sum, max), to reinforce
  the underlying logic
- `file_handling.py` — reading, writing, and appending to text files;
  parsing records and computing an average from file data
- `oop_basics.py` — classes, objects, and inheritance, modeled as a
  `Student` → `GraduateStudent` hierarchy with a `Course` class that
  aggregates and reports on a group of students

### NumPy
- `numpy_arrays.py` — indexing, slicing, boolean masking, and reshaping
- `numpy_matrix_ops.py` — dot product, matrix multiplication vs.
  element-wise multiplication, transpose, and matrix inverse
- `numpy_linalg.py` — solving `Ax = b` with `np.linalg.solve`,
  computing eigenvalues/eigenvectors with `np.linalg.eig` and verifying
  them manually against `A @ v = λv`, and computing determinants

## Notes

- Every NumPy result that has a "by hand" equivalent (dot product,
  determinant, eigenvalue check) is cross-verified manually in the
  same script — to confirm understanding of what NumPy was computing,
  not just calling the right function.
- Resources used: CS50P (cs50.harvard.edu), NumPy docs, 3Blue1Brown
  "Essence of Linear Algebra."

## Running

Each file is self-contained and runs standalone:

```bash
python3 numpy_linalg.py

# Week 2 – NumPy & Matplotlib

## Overview

This week focuses on learning **NumPy** for numerical computing and **Matplotlib** for data visualization. The programs cover mathematical operations, numerical methods, and different types of plots used in Data Science and Machine Learning.

---

## Topics Covered

### NumPy
- Arrays
- Mathematical Functions
- Numerical Computation
- Numerical Differentiation
- Linear Algebra Basics

### Matplotlib
- Line Plots
- Bar Charts
- Scatter Plots
- Histograms
- Pie Charts
- Multiple Subplots
- Plot Styling
- Figure Customization
- Saving Figures

---

## Programs

### Day 1 – Basic Plots
- Line Plot
- Bar Chart
- Scatter Plot

### Day 2 – Subplots & Styling
- Multiple Subplots
- Titles
- Labels
- Legends
- Grid
- Colors
- Figure Size

### Day 3 – Mathematical Functions
- Sine Graph
- Cosine Graph
- Exponential Function
- Logarithmic Function
- Polynomial Function

### Day 4 – Advanced Plots
- Histogram
- Pie Chart
- Box Plot
- Customized Charts

### Day 5 – NumPy + Matplotlib
- Random Data Visualization
- Statistical Graphs
- Array Visualization
- Combined Numerical Analysis

### Numerical Methods
- Numerical Differentiation
- Approximation Techniques
- Calculus using Python

---

## Skills Learned

- Data Visualization
- Numerical Computing
- Scientific Plotting
- Plot Customization
- Mathematical Modeling
- Working with Arrays
- Numerical Analysis
- Saving Graphs as Images

---

## Technologies Used

- Python 3
- NumPy
- Matplotlib
- Google Colab
- Git & GitHub

---

## Quick Start

```bash
pip install numpy matplotlib

python day1_basic_plots.py
python day2_subplots_styling.py
python day3_mathematical_functions.py
python day4_advanced_plots.py
python day5_numpy_matplotlib_combined.py
python calculus_numerical_methods.py
```

---

## Repository Structure

```
Week-2-NumPy-Matplotlib/
│
├── day1_basic_plots.py
├── day2_subplots_styling.py
├── day3_mathematical_functions.py
├── day4_advanced_plots.py
├── day5_numpy_matplotlib_combined.py
├── calculus_numerical_methods.py
└── README.md
```

---

## Learning Outcome

After completing Week 2, I can:

- Create professional data visualizations.
- Work with NumPy arrays efficiently.
- Plot mathematical functions.
- Customize charts and graphs.
- Perform basic numerical methods.
- Combine NumPy and Matplotlib for data analysis.
- Build visualization programs for Data Science and Machine Learning.

---

## Author

**Manoj Dio**

Learning Python, Data Analysis, Machine Learning, and Artificial Intelligence through hands-on coding practice.