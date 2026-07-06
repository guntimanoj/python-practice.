"""
Week 3 - Maths (Mon: 3B1B differential equations intro,
                Tue: first order ODEs, Wed: second order ODEs)

Covers:
- What a differential equation is (relates a function to its derivatives)
- Solving a first-order linear ODE analytically with SymPy: dy/dx = -k*y
- Solving a second-order ODE analytically with SymPy: y'' + y = 0 (simple harmonic motion)
- Comparing the analytical solution to a quick numerical check
"""

import sympy as sp
import numpy as np

x = sp.symbols("x")
y = sp.Function("y")

# ---------------------------------------------------------------------
# 1. First-order ODE: dy/dx = -k * y   (exponential decay, e.g. cooling, radioactive decay)
# ---------------------------------------------------------------------
k = sp.symbols("k", positive=True)
first_order_eq = sp.Eq(y(x).diff(x), -k * y(x))
first_order_solution = sp.dsolve(first_order_eq, y(x))

print("First-order ODE: dy/dx = -k*y")
print("Equation:", first_order_eq)
print("General solution:", first_order_solution)

# Apply initial condition y(0) = 100 to find the specific constant
C1 = sp.symbols("C1")
particular = first_order_solution.rhs.subs(x, 0)
c1_value = sp.solve(sp.Eq(particular, 100), C1)[0]
specific_solution = first_order_solution.rhs.subs(C1, c1_value)
print(f"With y(0) = 100: y(x) = {specific_solution}")

# Numeric sanity check at x=1, k=0.5
numeric_value = specific_solution.subs(k, 0.5).subs(x, 1).evalf()
print(f"At k=0.5, x=1: y = {numeric_value:.4f}  (expected ~ 100*e^-0.5 = {100*np.exp(-0.5):.4f})")

# ---------------------------------------------------------------------
# 2. Second-order ODE: y'' + y = 0   (simple harmonic motion, e.g. a spring)
# ---------------------------------------------------------------------
second_order_eq = sp.Eq(y(x).diff(x, 2) + y(x), 0)
second_order_solution = sp.dsolve(second_order_eq, y(x))

print("\nSecond-order ODE: y'' + y = 0")
print("Equation:", second_order_eq)
print("General solution:", second_order_solution)

# Apply initial conditions y(0) = 1, y'(0) = 0  -> should give y(x) = cos(x)
ics = {y(0): 1, y(x).diff(x).subs(x, 0): 0}
specific_second = sp.dsolve(second_order_eq, y(x), ics=ics)
print(f"With y(0)=1, y'(0)=0: {specific_second}")
print("(This matches the expected physical result: y(x) = cos(x), a spring oscillating"
      " with amplitude 1 and no phase shift.)")

# ---------------------------------------------------------------------
# 3. Quick numeric check of the second-order result against known cos(x) values
# ---------------------------------------------------------------------
check_points = [0, np.pi / 2, np.pi]
print("\nChecking y(x) = cos(x) at a few points:")
for point in check_points:
    val = specific_second.rhs.subs(x, point).evalf()
    print(f"  x = {point:.4f} -> y = {float(val):.4f}  (cos(x) = {np.cos(point):.4f})")