"""
Week 3 - Maths (Thu): Implement Euler's method in Python

Euler's method numerically approximates the solution to dy/dx = f(x, y)
given a starting point (x0, y0), by taking small steps of size h:

    y_next = y_current + h * f(x_current, y_current)

Test case: dy/dx = -k*y  (exponential decay), which has the known
analytical solution y(x) = y0 * exp(-k*x), so we can measure the error.
"""

import numpy as np


def euler_method(f, x0, y0, h, n_steps):
    """
    Approximate the solution of dy/dx = f(x, y) using Euler's method.

    Parameters
    ----------
    f       : function f(x, y) -> dy/dx
    x0, y0  : initial condition
    h       : step size
    n_steps : number of steps to take

    Returns
    -------
    xs, ys : numpy arrays of the x and approximated y values at each step
    """
    xs = np.zeros(n_steps + 1)
    ys = np.zeros(n_steps + 1)
    xs[0], ys[0] = x0, y0

    for i in range(n_steps):
        slope = f(xs[i], ys[i])
        ys[i + 1] = ys[i] + h * slope
        xs[i + 1] = xs[i] + h

    return xs, ys


if __name__ == "__main__":
    # dy/dx = -k * y, decay constant k = 0.5, y(0) = 100
    k = 0.5
    f = lambda x, y: -k * y

    x0, y0 = 0, 100
    h = 0.1
    n_steps = 50  # covers x from 0 to 5

    xs, ys_euler = euler_method(f, x0, y0, h, n_steps)
    ys_exact = y0 * np.exp(-k * xs)

    print(f"Euler's method for dy/dx = -{k}*y, y(0) = {y0}, step size h = {h}")
    print(f"{'x':>6} {'Euler y':>12} {'Exact y':>12} {'Abs Error':>12}")
    for i in range(0, n_steps + 1, 5):  # print every 5th step to keep it readable
        error = abs(ys_euler[i] - ys_exact[i])
        print(f"{xs[i]:6.2f} {ys_euler[i]:12.4f} {ys_exact[i]:12.4f} {error:12.4f}")

    max_error = np.max(np.abs(ys_euler - ys_exact))
    print(f"\nMax absolute error over the interval: {max_error:.4f}")

    # ------------------------------------------------------------------
    # Show that smaller step size -> smaller error (expected for Euler's method)
    # ------------------------------------------------------------------
    print("\nEffect of step size on accuracy (same interval, x: 0 to 5):")
    for h_test in [0.5, 0.1, 0.01]:
        n_test = int(5 / h_test)
        xs_t, ys_t = euler_method(f, x0, y0, h_test, n_test)
        exact_t = y0 * np.exp(-k * xs_t)
        err = np.max(np.abs(ys_t - exact_t))
        print(f"  h = {h_test:<5} -> max error = {err:.4f}")