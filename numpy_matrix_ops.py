import numpy as np


def dot_product_demo():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("Vector a:", a)
    print("Vector b:", b)
    print("Dot product a·b:", np.dot(a, b))
    manual = sum(a[i] * b[i] for i in range(len(a)))
    print("Manual check:", manual)


def matrix_multiplication_demo():
    A = np.array([
        [1, 2],
        [3, 4],
    ])
    B = np.array([
        [5, 6],
        [7, 8],
    ])
    print("\nMatrix A:\n", A)
    print("Matrix B:\n", B)
    print("A @ B (matrix multiplication):\n", A @ B)
    print("A * B (element-wise):\n", A * B)


def transpose_demo():
    M = np.array([
        [1, 2, 3],
        [4, 5, 6],
    ])
    print("\nOriginal matrix (2x3):\n", M)
    print("Transpose (3x2):\n", M.T)
    print("Shape before:", M.shape, "| Shape after:", M.T.shape)


def identity_and_inverse_demo():
    A = np.array([
        [4, 7],
        [2, 6],
    ], dtype=float)
    identity = np.eye(2)
    print("\nIdentity matrix:\n", identity)
    print("Matrix A:\n", A)

    A_inv = np.linalg.inv(A)
    print("Inverse of A:\n", A_inv)

    check = A @ A_inv
    print("A @ A_inv (should be identity):\n", np.round(check, 5))


if __name__ == "__main__":
    dot_product_demo()
    matrix_multiplication_demo()
    transpose_demo()
    identity_and_inverse_demo()