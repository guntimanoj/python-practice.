"""
SciPy Curve Fitting
Covers: linear fit, nonlinear (exponential) fit, fit with bounds,
        goodness of fit, and parameter uncertainty from covariance
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# 1. Linear model fit: y = m*x + c
# ---------------------------------------------------------
def linear_model(x, m, c):
    return m * x + c


def demo_linear_fit():
    rng = np.random.default_rng(0)
    x = np.linspace(0, 10, 50)
    true_m, true_c = 2.5, 1.0
    y = linear_model(x, true_m, true_c) + rng.normal(0, 1.5, size=x.size)

    popt, pcov = curve_fit(linear_model, x, y)
    perr = np.sqrt(np.diag(pcov))  # 1-sigma uncertainty on each parameter

    print("Linear fit: y = m*x + c")
    print(f"  m = {popt[0]:.3f} +/- {perr[0]:.3f} (true {true_m})")
    print(f"  c = {popt[1]:.3f} +/- {perr[1]:.3f} (true {true_c})\n")

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, s=15, label="Noisy data")
    plt.plot(x, linear_model(x, *popt), "r-", label="Fitted line")
    plt.legend()
    plt.title("Linear curve_fit")
    plt.savefig("linear_fit_demo.png", dpi=120)
    plt.close()


# ---------------------------------------------------------
# 2. Nonlinear model fit: exponential decay
# ---------------------------------------------------------
def exp_decay(x, a, k, b):
    return a * np.exp(-k * x) + b


def demo_exponential_fit():
    rng = np.random.default_rng(1)
    x = np.linspace(0, 5, 60)
    true_params = (3.0, 1.2, 0.5)
    y = exp_decay(x, *true_params) + rng.normal(0, 0.1, size=x.size)

    # initial guess matters for nonlinear fits
    p0 = (1.0, 1.0, 0.0)
    popt, pcov = curve_fit(exp_decay, x, y, p0=p0)
    perr = np.sqrt(np.diag(pcov))

    print("Exponential fit: y = a*exp(-k*x) + b")
    for name, val, err, true in zip("akb", popt, perr, true_params):
        print(f"  {name} = {val:.3f} +/- {err:.3f} (true {true})")
    print()

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, s=15, label="Noisy data")
    plt.plot(x, exp_decay(x, *popt), "r-", label="Fitted curve")
    plt.legend()
    plt.title("Exponential curve_fit")
    plt.savefig("exponential_fit_demo.png", dpi=120)
    plt.close()


# ---------------------------------------------------------
# 3. Fit with bounds (keeps parameters physically sensible)
# ---------------------------------------------------------
def demo_bounded_fit():
    rng = np.random.default_rng(2)
    x = np.linspace(0, 5, 60)
    true_params = (3.0, 1.2, 0.5)
    y = exp_decay(x, *true_params) + rng.normal(0, 0.1, size=x.size)

    # force a, k, b to stay non-negative
    popt, pcov = curve_fit(
        exp_decay, x, y,
        p0=(1.0, 1.0, 0.0),
        bounds=([0, 0, 0], [10, 10, 10]),
    )
    print("Bounded exponential fit (all params >= 0):")
    print(f"  a={popt[0]:.3f}, k={popt[1]:.3f}, b={popt[2]:.3f}\n")


# ---------------------------------------------------------
# 4. Goodness of fit: R-squared
# ---------------------------------------------------------
def r_squared(y_actual, y_predicted):
    ss_res = np.sum((y_actual - y_predicted) ** 2)
    ss_tot = np.sum((y_actual - np.mean(y_actual)) ** 2)
    return 1 - ss_res / ss_tot


def demo_goodness_of_fit():
    rng = np.random.default_rng(3)
    x = np.linspace(0, 5, 60)
    true_params = (3.0, 1.2, 0.5)
    y = exp_decay(x, *true_params) + rng.normal(0, 0.1, size=x.size)

    popt, _ = curve_fit(exp_decay, x, y, p0=(1.0, 1.0, 0.0))
    y_pred = exp_decay(x, *popt)

    r2 = r_squared(y, y_pred)
    print(f"Goodness of fit: R-squared = {r2:.4f}\n")


if __name__ == "__main__":
    demo_linear_fit()
    demo_exponential_fit()
    demo_bounded_fit()
    demo_goodness_of_fit()
    print("All curve fitting demos complete. PNG plots saved in this folder.")