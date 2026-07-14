import numpy as np

# Coefficient matrix
A = np.array([
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
])

# Constant matrix
B = np.array([8.0, -11.0, -3.0])

n = len(B)

# Forward Elimination
for i in range(n):

    # Pivoting (swap rows if needed)
    max_row = np.argmax(abs(A[i:, i])) + i
    A[[i, max_row]] = A[[max_row, i]]
    B[[i, max_row]] = B[[max_row, i]]

    # Eliminate below pivot
    for j in range(i + 1, n):
        factor = A[j, i] / A[i, i]
        A[j] = A[j] - factor * A[i]
        B[j] = B[j] - factor * B[i]

# Back Substitution
x = np.zeros(n)

for i in range(n - 1, -1, -1):
    x[i] = (B[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

print("Solution:")
print(x)