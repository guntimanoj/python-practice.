"""
SciPy — Optimization and Root Finding
=====================================================

Covers:
  1. Scalar root finding: bisect, brentq, newton
  2. Systems of nonlinear equations: scipy.optimize.root
  3. Unconstrained optimization: scipy.optimize.minimize (Nelder-Mead, BFGS)
  4. Constrained optimization: bounds + constraints in minimize
  5. Linear programming: scipy.optimize.linprog

Run: python optimization_rootfinding.py
"""

import numpy as np
from scipy.optimize import (
    bisect, brentq, newton,
    root, minimize, linprog
)
import matplotlib.pyplot as plt


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------
# 1. SCALAR ROOT FINDING
# ---------------------------------------------------------------
def scalar_root_finding():
    section("1. Scalar Root Finding")

    # f(x) = x^3 - x - 2  -> find root near x = 1.5
    def f(x):
        return x**3 - x - 2

    def fprime(x):
        return 3 * x**2 - 1

    # Bisection: needs a bracket [a, b] where f(a) and f(b) have opposite signs
    root_bisect = bisect(f, 1, 2)
    print(f"bisect:  root = {root_bisect:.8f}, f(root) = {f(root_bisect):.2e}")

    # Brent's method: faster, more robust bracketing method (preferred default)
    root_brentq = brentq(f, 1, 2)
    print(f"brentq:  root = {root_brentq:.8f}, f(root) = {f(root_brentq):.2e}")

    # Newton-Raphson: needs only an initial guess (and optionally derivative)
    root_newton = newton(f, x0=1.5, fprime=fprime)
    print(f"newton:  root = {root_newton:.8f}, f(root) = {f(root_newton):.2e}")

    # Newton without derivative -> falls back to secant method
    root_secant = newton(f, x0=1.5)
    print(f"secant:  root = {root_secant:.8f}, f(root) = {f(root_secant):.2e}")

    # Visualize
    x = np.linspace(-2, 3, 400)
    plt.figure(figsize=(7, 4))
    plt.axhline(0, color="gray", lw=0.8)
    plt.plot(x, f(x), label=r"$f(x) = x^3 - x - 2$")
    plt.plot(root_brentq, f(root_brentq), "ro", label=f"root ≈ {root_brentq:.4f}")
    plt.title("Scalar Root Finding")
    plt.xlabel("x"); plt.ylabel("f(x)")
    plt.legend(); plt.grid(alpha=0.3)
    plt.savefig("scalar_root_finding.png", dpi=120, bbox_inches="tight")
    plt.close()
    print("Saved plot -> scalar_root_finding.png")


# ---------------------------------------------------------------
# 2. SYSTEMS OF NONLINEAR EQUATIONS
# ---------------------------------------------------------------
def system_root_finding():
    section("2. Systems of Nonlinear Equations (scipy.optimize.root)")

    # Solve:
    #   x^2 + y^2 = 4
    #   x*y = 1
    def system(vars):
        x, y = vars
        return [x**2 + y**2 - 4, x * y - 1]

    sol = root(system, x0=[1, 1], method="hybr")
    print("method = hybr")
    print(f"  success: {sol.success}")
    print(f"  x, y   = {sol.x}")
    print(f"  residual = {system(sol.x)}")

    # Levenberg-Marquardt as alternative method
    sol_lm = root(system, x0=[1, 1], method="lm")
    print("\nmethod = lm")
    print(f"  success: {sol_lm.success}")
    print(f"  x, y   = {sol_lm.x}")


# ---------------------------------------------------------------
# 3. UNCONSTRAINED OPTIMIZATION
# ---------------------------------------------------------------
def unconstrained_optimization():
    section("3. Unconstrained Optimization (scipy.optimize.minimize)")

    # Rosenbrock function: classic optimization test case
    # Global minimum at (1, 1), f = 0
    def rosenbrock(v):
        x, y = v
        return (1 - x)**2 + 100 * (y - x**2)**2

    x0 = [-1.2, 1.0]

    for method in ["Nelder-Mead", "BFGS", "Powell"]:
        result = minimize(rosenbrock, x0, method=method)
        print(f"{method:12s}: x* = {result.x}, f(x*) = {result.fun:.6e}, "
              f"iters = {result.nit if hasattr(result, 'nit') else 'n/a'}")


# ---------------------------------------------------------------
# 4. CONSTRAINED OPTIMIZATION
# ---------------------------------------------------------------
def constrained_optimization():
    section("4. Constrained Optimization")

    # Minimize f(x, y) = x^2 + y^2
    # subject to: x + y = 1  (equality constraint)
    #             x >= 0, y >= 0  (bounds)
    def objective(v):
        x, y = v
        return x**2 + y**2

    constraints = {"type": "eq", "fun": lambda v: v[0] + v[1] - 1}
    bounds = [(0, None), (0, None)]

    result = minimize(
        objective, x0=[0.5, 0.5],
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )
    print(f"success: {result.success}")
    print(f"x* = {result.x}, f(x*) = {result.fun:.6f}")
    print("(Analytical answer: x = y = 0.5, f = 0.5)")


# ---------------------------------------------------------------
# 5. LINEAR PROGRAMMING
# ---------------------------------------------------------------
def linear_programming():
    section("5. Linear Programming (scipy.optimize.linprog)")

    # Minimize: c^T x = -x1 - 2*x2  (i.e. maximize x1 + 2*x2)
    # Subject to:
    #   x1 + x2 <= 4
    #   x1 + 3*x2 <= 6
    #   x1, x2 >= 0
    c = [-1, -2]
    A_ub = [[1, 1], [1, 3]]
    b_ub = [4, 6]
    bounds = [(0, None), (0, None)]

    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
    print(f"success: {result.success}")
    print(f"x* = {result.x}")
    print(f"max(x1 + 2*x2) = {-result.fun:.4f}")


# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
if __name__ == "__main__":
    scalar_root_finding()
    system_root_finding()
    unconstrained_optimization()
    constrained_optimization()
    linear_programming()
    print("\nDone. All sections executed successfully.")