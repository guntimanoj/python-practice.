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