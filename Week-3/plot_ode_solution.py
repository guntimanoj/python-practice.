"""
Week 3 - Maths: Plot ODE solution with Matplotlib

Builds on 07_euler_method.py: plots the Euler approximation against the
exact analytical solution, and also solves a slightly harder ODE
(logistic growth) using SciPy's solve_ivp for comparison.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# euler_method is re-implemented here (rather than imported from 07_euler_method.py)
# so this script can run standalone regardless of filename/module-import quirks.
def euler_method(f, x0, y0, h, n_steps):
    xs = np.zeros(n_steps + 1)
    ys = np.zeros(n_steps + 1)
    xs[0], ys[0] = x0, y0
    for i in range(n_steps):
        ys[i + 1] = ys[i] + h * f(xs[i], ys[i])
        xs[i + 1] = xs[i] + h
    return xs, ys


# ---------------------------------------------------------------------
# 1. Plot 1: Euler approximation vs exact solution for dy/dx = -k*y
# ---------------------------------------------------------------------
k = 0.5
f_decay = lambda x, y: -k * y
x0, y0 = 0, 100
h = 0.3
n_steps = int(5 / h)

xs_euler, ys_euler = euler_method(f_decay, x0, y0, h, n_steps)
xs_fine = np.linspace(0, 5, 300)
ys_exact = y0 * np.exp(-k * xs_fine)

plt.figure(figsize=(7, 4.5))
plt.plot(xs_fine, ys_exact, label="Exact solution: $y = 100e^{-0.5x}$", color="black", linewidth=2)
plt.plot(xs_euler, ys_euler, "o--", label=f"Euler approximation (h={h})", color="tomato")
plt.title("Exponential Decay: Euler's Method vs Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ode_decay_euler_vs_exact.png", dpi=120)
plt.close()
print("Saved: ode_decay_euler_vs_exact.png")

# ---------------------------------------------------------------------
# 2. Plot 2: Error convergence as step size h shrinks
# ---------------------------------------------------------------------
h_values = [0.5, 0.25, 0.1, 0.05, 0.01, 0.005]
max_errors = []
for h_test in h_values:
    n_test = int(5 / h_test)
    xs_t, ys_t = euler_method(f_decay, x0, y0, h_test, n_test)
    exact_t = y0 * np.exp(-k * xs_t)
    max_errors.append(np.max(np.abs(ys_t - exact_t)))

plt.figure(figsize=(6, 4.5))
plt.loglog(h_values, max_errors, "o-", color="steelblue")
plt.title("Euler's Method: Error Shrinks as Step Size Decreases")
plt.xlabel("Step size h (log scale)")
plt.ylabel("Max absolute error (log scale)")
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()
plt.savefig("ode_euler_error_convergence.png", dpi=120)
plt.close()
print("Saved: ode_euler_error_convergence.png")
print("\nStep size vs max error:")
for h_test, err in zip(h_values, max_errors):
    print(f"  h = {h_test:<6} -> max error = {err:.5f}")

# ---------------------------------------------------------------------
# 3. Plot 3: A nonlinear ODE - logistic growth, solved with SciPy solve_ivp
#    dy/dt = r * y * (1 - y/K)   (population growth with a carrying capacity)
# ---------------------------------------------------------------------
r, K = 0.8, 100
y0_logistic = 5

def logistic(t, y):
    return r * y * (1 - y / K)

t_span = (0, 20)
t_eval = np.linspace(*t_span, 200)
sol = solve_ivp(logistic, t_span, [y0_logistic], t_eval=t_eval)

plt.figure(figsize=(7, 4.5))
plt.plot(sol.t, sol.y[0], color="seagreen", linewidth=2)
plt.axhline(K, color="gray", linestyle="--", label=f"Carrying capacity K={K}")
plt.title("Logistic Growth ODE (solved with SciPy solve_ivp)")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ode_logistic_growth.png", dpi=120)
plt.close()
print("\nSaved: ode_logistic_growth.png")
print(f"Population approaches carrying capacity K={K} as t -> infinity.")
print(f"Population at t=20: {sol.y[0][-1]:.2f}")