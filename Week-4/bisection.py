"""
Bisection Method for Root Finding
=================================
Finds a root of a continuous function f(x) in an interval [a, b]
where f(a) and f(b) have opposite signs.
"""

import matplotlib.pyplot as plt
import numpy as np


def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    Find a root of f in [a, b] using the bisection method.

    Parameters
    ----------
    f : callable
        Continuous function whose root is sought.
    a, b : float
        Interval endpoints with f(a) and f(b) of opposite sign.
    tol : float
        Stopping tolerance on the interval width / |f(c)|.
    max_iter : int
        Maximum number of iterations allowed.

    Returns
    -------
    root : float
        Approximate root.
    history : list of dict
        Iteration history (for plotting/analysis), each entry has
        keys: 'iter', 'a', 'b', 'c', 'f(c)'.
    """
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    history = []
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        history.append({"iter": i, "a": a, "b": b, "c": c, "f(c)": fc})

        if abs(fc) < tol or (b - a) / 2 < tol:
            break

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return c, history


def plot_bisection(f, a, b, history, title="Bisection Method"):
    """Plot the function and the sequence of bisection midpoints."""
    xs = np.linspace(a - 0.5, b + 0.5, 400)
    ys = [f(x) for x in xs]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left plot: function curve + midpoints converging to the root
    ax = axes[0]
    ax.axhline(0, color="black", linewidth=0.8)
    ax.plot(xs, ys, label="f(x)", color="steelblue")
    mids = [h["c"] for h in history]
    fmids = [h["f(c)"] for h in history]
    ax.scatter(mids, fmids, color="crimson", s=25, zorder=5, label="midpoints")
    ax.plot(mids[-1], fmids[-1], marker="*", color="gold",
            markersize=18, zorder=6, label="final root estimate")
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(alpha=0.3)

    # Right plot: convergence of the midpoint estimate over iterations
    ax2 = axes[1]
    iters = [h["iter"] for h in history]
    ax2.plot(iters, mids, marker="o", color="darkgreen")
    ax2.axhline(mids[-1], color="gray", linestyle="--", linewidth=1,
                label=f"converged ≈ {mids[-1]:.6f}")
    ax2.set_title("Convergence of Root Estimate")
    ax2.set_xlabel("Iteration")
    ax2.set_ylabel("Midpoint c")
    ax2.legend()
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("bisection_plot.png", dpi=150)
    print("Saved plot to bisection_plot.png")


if __name__ == "__main__":
    # Example: find root of f(x) = x^3 - x - 2 in [1, 2]
    f = lambda x: x**3 - x - 2

    root, history = bisection(f, 1, 2, tol=1e-8)

    print(f"Converged root ≈ {root:.8f} after {len(history)} iterations")
    for h in history:
        print(f"  iter {h['iter']:2d}: a={h['a']:.6f}, b={h['b']:.6f}, "
              f"c={h['c']:.6f}, f(c)={h['f(c)']:.2e}")

    plot_bisection(f, 1, 2, history, title="Root of f(x) = x^3 - x - 2")