"""
Newton-Raphson Method
--------------------------------------------------------
Implements the Newton-Raphson root-finding method from scratch,
then verifies it against scipy.optimize.newton.

Newton-Raphson formula:
    x_(n+1) = x_n - f(x_n) / f'(x_n)
"""

import numpy as np
import matplotlib.pyplot as plt


def newton_raphson(f, f_prime, x0, tol=1e-8, max_iter=100, verbose=True):
    """
    Find a root of f(x) = 0 using the Newton-Raphson method.

    Parameters:
        f        : function whose root we want
        f_prime  : derivative of f
        x0       : initial guess
        tol      : stopping tolerance on |f(x)|
        max_iter : maximum number of iterations

    Returns:
        root, history (list of x values at each iteration)
    """
    x = x0
    history = [x]

    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)

        if fpx == 0:
            raise ZeroDivisionError(f"Derivative is zero at x = {x}, cannot continue.")

        x_new = x - fx / fpx
        history.append(x_new)

        if verbose:
            print(f"Iteration {i+1}: x = {x_new:.10f}, f(x) = {f(x_new):.2e}")

        if abs(f(x_new)) < tol:
            return x_new, history

        x = x_new

    raise RuntimeError(f"Did not converge within {max_iter} iterations.")


# ===========================================================
# Example 1: Find root of f(x) = x^2 - 2  (i.e. sqrt(2))
# ===========================================================
def f1(x):
    return x**2 - 2

def f1_prime(x):
    return 2 * x

print("=" * 60)
print("Example 1: Root of x^2 - 2 = 0  (expected: sqrt(2) = 1.41421356)")
print("=" * 60)
root1, history1 = newton_raphson(f1, f1_prime, x0=1.0)
print(f"\nRoot found: {root1:.10f}")
print(f"True value: {np.sqrt(2):.10f}")
print(f"Iterations to converge: {len(history1) - 1}")


# ===========================================================
# Example 2: Find root of f(x) = x^3 - x - 2
# ===========================================================
def f2(x):
    return x**3 - x - 2

def f2_prime(x):
    return 3 * x**2 - 1

print("\n" + "=" * 60)
print("Example 2: Root of x^3 - x - 2 = 0")
print("=" * 60)
root2, history2 = newton_raphson(f2, f2_prime, x0=1.5)
print(f"\nRoot found: {root2:.10f}")

# Verify against SciPy
from scipy.optimize import newton
scipy_root = newton(f2, x0=1.5, fprime=f2_prime)
print(f"SciPy's newton() result: {scipy_root:.10f}")


# ===========================================================
# Example 3: Convergence visualization
# ===========================================================
def f3(x):
    return np.cos(x) - x

def f3_prime(x):
    return -np.sin(x) - 1

print("\n" + "=" * 60)
print("Example 3: Root of cos(x) - x = 0")
print("=" * 60)
root3, history3 = newton_raphson(f3, f3_prime, x0=0.5)
print(f"\nRoot found: {root3:.10f}")

# Plot convergence and function
fig, axs = plt.subplots(1, 2, figsize=(12, 4.5))

# Function curve with root marked
x_vals = np.linspace(-1, 2, 300)
axs[0].plot(x_vals, f3(x_vals), label='f(x) = cos(x) - x')
axs[0].axhline(0, color='gray', linestyle='--', linewidth=0.8)
axs[0].plot(root3, 0, 'ro', label=f'Root ≈ {root3:.4f}')
axs[0].plot(history3, [f3(x) for x in history3], 'g.--', alpha=0.6, label='Newton steps')
axs[0].set_title("Newton-Raphson: Function and Root")
axs[0].set_xlabel("x")
axs[0].set_ylabel("f(x)")
axs[0].legend()

# Convergence of error per iteration
errors = [abs(x - root3) for x in history3]
axs[1].semilogy(range(len(errors)), errors, 'o-')
axs[1].set_title("Convergence Rate (log scale)")
axs[1].set_xlabel("Iteration")
axs[1].set_ylabel("|x_n - root|")

plt.tight_layout()
plt.savefig("newton_raphson_results.png", dpi=150)
plt.show()

print("\nPlot saved as newton_raphson_results.png")
print("\nNote: Newton-Raphson converges quadratically -- notice how the")
print("error roughly squares (halves the number of correct digits doubling)")
print("each iteration once close to the root.")