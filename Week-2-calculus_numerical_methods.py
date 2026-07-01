"""
Week 2 Calculus: Numerical Derivatives and Integration
Implements calculus concepts from Khan Academy in Python
Run: python calculus_numerical_methods.py
"""

import matplotlib.pyplot as plt
import numpy as np

print("Implementing numerical calculus methods...")

# ==================== NUMERICAL DERIVATIVES ====================
print("Computing numerical derivatives...")

def f(x):
    """Example function: f(x) = x^3 - 2x^2 + x + 5"""
    return x**3 - 2*x**2 + x + 5

def f_analytical_derivative(x):
    """Analytical derivative: f'(x) = 3x^2 - 4x + 1"""
    return 3*x**2 - 4*x + 1

def numerical_derivative_forward(func, x, h=1e-5):
    """Forward difference: f'(x) ≈ (f(x+h) - f(x)) / h"""
    return (func(x + h) - func(x)) / h

def numerical_derivative_backward(func, x, h=1e-5):
    """Backward difference: f'(x) ≈ (f(x) - f(x-h)) / h"""
    return (func(x) - func(x - h)) / h

def numerical_derivative_central(func, x, h=1e-5):
    """Central difference: f'(x) ≈ (f(x+h) - f(x-h)) / (2h)"""
    return (func(x + h) - func(x - h)) / (2 * h)

# Create visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Numerical Derivatives - Calculus Week 2', fontsize=16, fontweight='bold')

# Plot 1: Function and its derivative
x = np.linspace(-2, 3, 300)
y = f(x)
y_prime = f_analytical_derivative(x)

ax = axes[0, 0]
ax.plot(x, y, label='f(x) = x³ - 2x² + x + 5', linewidth=2.5, color='blue')
ax.plot(x, y_prime, label="f'(x) = 3x² - 4x + 1", linewidth=2.5, color='red')
ax.fill_between(x, y, alpha=0.2, color='blue')
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.set_title('Function and Analytical Derivative', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')

# Plot 2: Comparison of numerical methods at a point
ax = axes[0, 1]
x_point = 1.0
h_values = np.logspace(-10, -1, 50)
errors = {
    'Forward': [],
    'Backward': [],
    'Central': []
}

true_derivative = f_analytical_derivative(x_point)

for h in h_values:
    errors['Forward'].append(np.abs(numerical_derivative_forward(f, x_point, h) - true_derivative))
    errors['Backward'].append(np.abs(numerical_derivative_backward(f, x_point, h) - true_derivative))
    errors['Central'].append(np.abs(numerical_derivative_central(f, x_point, h) - true_derivative))

ax.loglog(h_values, errors['Forward'], 'o-', label='Forward difference', linewidth=2, markersize=4, alpha=0.7)
ax.loglog(h_values, errors['Backward'], 's-', label='Backward difference', linewidth=2, markersize=4, alpha=0.7)
ax.loglog(h_values, errors['Central'], '^-', label='Central difference', linewidth=2.5, markersize=5, alpha=0.8)
ax.set_xlabel('Step size h (log scale)', fontsize=11)
ax.set_ylabel('Absolute Error (log scale)', fontsize=11)
ax.set_title('Numerical Derivative Error vs Step Size\nat x=1', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, which='both')
ax.set_facecolor('#f8f9fa')

# Plot 3: Derivative approximation at multiple points
ax = axes[1, 0]
x_test = np.linspace(-2, 3, 50)
dy_analytical = f_analytical_derivative(x_test)
dy_numerical_central = [numerical_derivative_central(f, xi, h=1e-6) for xi in x_test]

ax.plot(x_test, dy_analytical, 'o-', label='Analytical derivative', linewidth=2.5, 
        markersize=6, color='red', alpha=0.8, markevery=5)
ax.plot(x_test, dy_numerical_central, 's--', label='Numerical (central diff)', linewidth=2, 
        markersize=5, color='blue', alpha=0.6, markevery=5)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel("f'(x)", fontsize=11)
ax.set_title('Analytical vs Numerical Derivative', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')

# Plot 4: Chain rule visualization
ax = axes[1, 1]

def g(x):
    """g(x) = sin(x)"""
    return np.sin(x)

def h(x):
    """h(x) = x^2"""
    return x**2

def composite(x):
    """f(x) = g(h(x)) = sin(x^2)"""
    return np.sin(x**2)

def composite_derivative_analytical(x):
    """f'(x) = g'(h(x)) * h'(x) = cos(x^2) * 2x"""
    return np.cos(x**2) * 2*x

x = np.linspace(-2, 2, 300)
y_composite = composite(x)
dy_composite = composite_derivative_analytical(x)
dy_numerical = np.array([numerical_derivative_central(composite, xi, h=1e-6) for xi in x])

ax.plot(x, y_composite, linewidth=2.5, color='purple', label='f(x) = sin(x²)')
ax.plot(x, dy_composite, linewidth=2.5, color='orange', label="f'(x) = cos(x²)·2x (analytical)")
ax.plot(x, dy_numerical, 'o-', linewidth=1.5, markersize=3, color='green', alpha=0.6, 
        markevery=20, label="f'(x) numerical")
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.set_title('Chain Rule: f(x) = sin(x²)', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')

plt.tight_layout()
plt.savefig('calculus_numerical_derivatives.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Numerical derivatives visualization saved")

# ==================== NUMERICAL INTEGRATION ====================
print("Computing numerical integration...")

def integrand(x):
    """Example: f(x) = exp(-x^2) (Gaussian)"""
    return np.exp(-x**2)

def numerical_integration_rectangle(func, a, b, n=1000):
    """Rectangle rule (Riemann sum)"""
    x = np.linspace(a, b, n)
    dx = (b - a) / n
    return np.sum(func(x[:-1])) * dx

def numerical_integration_trapezoid(func, a, b, n=1000):
    """Trapezoidal rule"""
    x = np.linspace(a, b, n+1)
    dx = (b - a) / n
    return (dx/2) * (func(x[0]) + 2*np.sum(func(x[1:-1])) + func(x[-1]))

def numerical_integration_simpson(func, a, b, n=1000):
    """Simpson's rule"""
    if n % 2 == 1:
        n += 1
    x = np.linspace(a, b, n+1)
    dx = (b - a) / n
    return (dx/3) * (func(x[0]) + 4*np.sum(func(x[1:-1:2])) + 2*np.sum(func(x[2:-1:2])) + func(x[-1]))

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Numerical Integration - Calculus Week 2', fontsize=16, fontweight='bold')

# Plot 1: Rectangle rule visualization
ax = axes[0, 0]
x = np.linspace(-2, 2, 300)
y = integrand(x)
ax.plot(x, y, linewidth=2.5, color='blue', label='f(x) = e^(-x²)')
ax.fill_between(x, y, alpha=0.3, color='blue')

# Show rectangles
x_rect = np.linspace(-2, 2, 21)
dx_rect = (2 - (-2)) / 20
for xi in x_rect[:-1]:
    ax.bar(xi, integrand(xi), width=dx_rect, alpha=0.2, color='red', edgecolor='red', linewidth=0.5)

ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('f(x)', fontsize=11)
ax.set_title('Rectangle Rule (Riemann Sum)\nn=20 rectangles', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')

# Plot 2: Comparison of integration methods
ax = axes[0, 1]
n_values = np.logspace(1, 4, 30, dtype=int)
a, b = -3, 3

# True value (numerical approximation with high n)
true_integral = numerical_integration_simpson(integrand, a, b, n=10000)

errors_rect = []
errors_trap = []
errors_simp = []

for n in n_values:
    errors_rect.append(np.abs(numerical_integration_rectangle(integrand, a, b, n) - true_integral))
    errors_trap.append(np.abs(numerical_integration_trapezoid(integrand, a, b, n) - true_integral))
    errors_simp.append(np.abs(numerical_integration_simpson(integrand, a, b, n) - true_integral))

ax.loglog(n_values, errors_rect, 'o-', label='Rectangle rule', linewidth=2, markersize=5, alpha=0.7)
ax.loglog(n_values, errors_trap, 's-', label='Trapezoidal rule', linewidth=2, markersize=5, alpha=0.7)
ax.loglog(n_values, errors_simp, '^-', label='Simpson\'s rule', linewidth=2.5, markersize=6, alpha=0.8)
ax.set_xlabel('Number of intervals n (log scale)', fontsize=11)
ax.set_ylabel('Absolute Error (log scale)', fontsize=11)
ax.set_title('Integration Error Convergence', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, which='both')
ax.set_facecolor('#f8f9fa')

# Plot 3: Trapezoid rule visualization
ax = axes[1, 0]
x = np.linspace(-2, 2, 300)
y = integrand(x)
ax.plot(x, y, linewidth=2.5, color='blue', label='f(x) = e^(-x²)')

# Show trapezoids
x_trap = np.linspace(-2, 2, 16)
for i in range(len(x_trap)-1):
    x_trap_section = np.linspace(x_trap[i], x_trap[i+1], 100)
    y_trap_section = integrand(x_trap_section)
    ax.fill_between(x_trap_section, y_trap_section, alpha=0.2, color='green')
    # Draw trapezoid outlines
    ax.plot([x_trap[i], x_trap[i+1]], [integrand(x_trap[i]), integrand(x_trap[i+1])], 
            color='green', linewidth=1.5, alpha=0.7)

ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('f(x)', fontsize=11)
ax.set_title('Trapezoidal Rule\nn=15 trapezoids', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')

# Plot 4: Different integrand
ax = axes[1, 1]

def integrand2(x):
    """f(x) = 1/(1+x^2)"""
    return 1 / (1 + x**2)

x = np.linspace(-5, 5, 300)
y = integrand2(x)
ax.plot(x, y, linewidth=2.5, color='red', label='f(x) = 1/(1+x²)')
ax.fill_between(x, y, alpha=0.3, color='red')

# Compute integral analytically (arctan)
analytical_integral = np.arctan(5) - np.arctan(-5)
numerical_integral = numerical_integration_simpson(integrand2, -5, 5, n=1000)

textstr = f'∫₋₅⁵ 1/(1+x²) dx\nAnalytical: {analytical_integral:.6f}\nNumerical (Simpson): {numerical_integral:.6f}\nError: {abs(analytical_integral - numerical_integral):.2e}'
ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=10, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('f(x)', fontsize=11)
ax.set_title('Integration: arctan(x)', fontsize=12, fontweight='bold')
ax.legend(fontsize=10, loc='upper right')
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')

plt.tight_layout()
plt.savefig('calculus_numerical_integration.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Numerical integration visualization saved")

# Print some results
print("\n" + "="*60)
print("NUMERICAL CALCULUS RESULTS")
print("="*60)

print("\nNumerical Derivative Example at x=1:")
print(f"  Analytical: f'(1) = {f_analytical_derivative(1):.8f}")
print(f"  Forward diff: {numerical_derivative_forward(f, 1):.8f}")
print(f"  Central diff: {numerical_derivative_central(f, 1):.8f}")

print("\nNumerical Integration Example: ∫₋₃³ e^(-x²) dx")
print(f"  Rectangle rule (n=1000): {numerical_integration_rectangle(integrand, -3, 3):.8f}")
print(f"  Trapezoidal rule (n=1000): {numerical_integration_trapezoid(integrand, -3, 3):.8f}")
print(f"  Simpson's rule (n=1000): {numerical_integration_simpson(integrand, -3, 3):.8f}")

print("\nNumerical Integration Example: ∫₋₅⁵ 1/(1+x²) dx")
analytical = np.arctan(5) - np.arctan(-5)
numerical_simp = numerical_integration_simpson(integrand2, -5, 5)
print(f"  Analytical (arctan): {analytical:.8f}")
print(f"  Simpson's rule (n=1000): {numerical_simp:.8f}")
print(f"  Error: {abs(analytical - numerical_simp):.2e}")

print("\n✓ All calculus numerical methods implemented successfully!")