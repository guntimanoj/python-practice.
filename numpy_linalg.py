import numpy as np


def solve_linear_system():
    """
    Solve the system:
        2x + y = 5
        x + 3y = 10
    i.e. Ax = b
    """
    A = np.array([
        [2, 1],
        [1, 3],
    ])
    b = np.array([5, 10])

    x = np.linalg.solve(A, b)
    print("A:\n", A)
    print("b:", b)
    print("Solution x:", x)

    check = A @ x
    print("A @ x (should equal b):", check)


def eigenvalues_demo():
    """
    Find eigenvalues/eigenvectors of a symmetric matrix,
    then verify manually using A @ v = lambda * v.
    """
    A = np.array([
        [4, 2],
        [1, 3],
    ], dtype=float)

    eigenvalues, eigenvectors = np.linalg.eig(A)
    print("\nMatrix A:\n", A)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors (columns):\n", eigenvectors)

    for i in range(len(eigenvalues)):
        lam = eigenvalues[i]
        v = eigenvectors[:, i]
        lhs = A @ v
        rhs = lam * v
        print(f"\nCheck eigenpair {i}:")
        print("  A @ v   =", lhs)
        print("  lambda*v =", rhs)


def determinant_demo():
    A = np.array([
        [2, 1],
        [1, 3],
    ])
    det = np.linalg.det(A)
    print("\nMatrix A:\n", A)
    print("Determinant:", det)
    manual_det = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    print("Manual check (ad - bc):", manual_det)


if __name__ == "__main__":
    solve_linear_system()
    eigenvalues_demo()
    determinant_demo()