
import matplotlib.pyplot as plt
import numpy as np

print("Generating mathematical function plots...")

# ==================== POLYNOMIAL FUNCTIONS ====================
print("Plotting polynomial functions...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Mathematical Functions - Day 3', fontsize=16, fontweight='bold')

x = np.linspace(-3, 3, 200)

# Linear: y = mx + c
ax = axes[0, 0]
for m, c in [(1, 0), (2, 1), (-1, -1)]:
    y = m*x + c
    ax.plot(x, y, label=f'y = {m}x + {c}', linewidth=2.5)
ax.set_title('Linear Functions', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)

# Quadratic: y = ax^2 + bx + c
ax = axes[0, 1]
for a, b, c in [(1, 0, 0), (0.5, 1, 0), (-1, 0, 2)]:
    y = a*x**2 + b*x + c
    ax.plot(x, y, label=f'y = {a}x² + {b}x + {c}', linewidth=2.5)
ax.set_title('Quadratic Functions', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)

# Cubic: y = x^3
ax = axes[1, 0]
y_cubic = x**3
ax.plot(x, y_cubic, label='y = x³', linewidth=2.5, color='#e74c3c')
ax.fill_between(x, y_cubic, alpha=0.2, color='#e74c3c')
ax.set_title('Cubic Function', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)

# Reciprocal: y = 1/x
ax = axes[1, 1]
x_positive = np.linspace(0.1, 4, 200)
x_negative = np.linspace(-4, -0.1, 200)
ax.plot(x_positive, 1/x_positive, label='y = 1/x (positive)', linewidth=2.5, color='#3498db')
ax.plot(x_negative, 1/x_negative, label='y = 1/x (negative)', linewidth=2.5, color='#3498db')
ax.set_title('Reciprocal Function (with asymptote)', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_ylim(-10, 10)
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5, linestyle='--', alpha=0.5)
ax.set_facecolor('#f8f9fa')

plt.tight_layout()
plt.savefig('day3_polynomial_functions.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Polynomial functions saved")

# ==================== TRIGONOMETRIC & EXPONENTIAL ====================
print("Plotting trigonometric and exponential functions...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Trigonometric & Exponential Functions - Day 3', fontsize=16, fontweight='bold')

x = np.linspace(0, 4*np.pi, 200)

# Sine and Cosine
ax = axes[0, 0]
ax.plot(x, np.sin(x), label='sin(x)', linewidth=2.5, color='#e74c3c')
ax.plot(x, np.cos(x), label='cos(x)', linewidth=2.5, color='#3498db')
ax.fill_between(x, np.sin(x), alpha=0.2, color='#e74c3c')
ax.set_title('Sine and Cosine', fontsize=12, fontweight='bold')
ax.set_xlabel('Radians')
ax.set_ylabel('Value')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')
ax.set_xticks([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
ax.set_xticklabels(['0', 'π', '2π', '3π', '4π'])

# Tangent
ax = axes[0, 1]
x_tan = np.linspace(-np.pi/2 + 0.1, np.pi/2 - 0.1, 200)
ax.plot(x_tan, np.tan(x_tan), linewidth=2.5, color='#2ecc71')
ax.axvline(x=-np.pi/2, color='red', linestyle='--', linewidth=1, alpha=0.5, label='Asymptotes')
ax.axvline(x=np.pi/2, color='red', linestyle='--', linewidth=1, alpha=0.5)
ax.set_title('Tangent Function', fontsize=12, fontweight='bold')
ax.set_xlabel('Radians')
ax.set_ylabel('tan(x)')
ax.set_ylim(-10, 10)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')
ax.legend(fontsize=10)

# Exponential: e^x
ax = axes[1, 0]
x_exp = np.linspace(-2, 3, 200)
ax.plot(x_exp, np.exp(x_exp), label='e^x', linewidth=2.5, color='#e74c3c')
ax.fill_between(x_exp, np.exp(x_exp), alpha=0.2, color='#e74c3c')
ax.set_title('Exponential Function', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('e^x')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')

# Logarithm: ln(x)
ax = axes[1, 1]
x_log = np.linspace(0.1, 5, 200)
ax.plot(x_log, np.log(x_log), label='ln(x)', linewidth=2.5, color='#9b59b6')
ax.fill_between(x_log, np.log(x_log), alpha=0.2, color='#9b59b6')
ax.axvline(x=0, color='red', linestyle='--', linewidth=1, alpha=0.5, label='Asymptote')
ax.axhline(y=0, color='k', linewidth=0.5)
ax.set_title('Logarithmic Function', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('ln(x)')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')

plt.tight_layout()
plt.savefig('day3_trigonometric_exponential.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Trigonometric and exponential functions saved")

# ==================== COMPOSITE FUNCTIONS ====================
print("Plotting composite functions...")
fig, ax = plt.subplots(figsize=(12, 7))

x = np.linspace(-2*np.pi, 2*np.pi, 300)
y1 = np.sin(x) * np.exp(-x**2/10)
y2 = np.cos(x) * np.exp(-x**2/10)

ax.plot(x, y1, label='sin(x)·e^(-x²/10)', linewidth=2.5, color='#e74c3c')
ax.plot(x, y2, label='cos(x)·e^(-x²/10)', linewidth=2.5, color='#3498db')
ax.fill_between(x, y1, alpha=0.2, color='#e74c3c')
ax.fill_between(x, y2, alpha=0.2, color='#3498db')

ax.set_title('Composite Functions: Trigonometric × Exponential Decay', fontsize=14, fontweight='bold')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.legend(fontsize=11, loc='upper right')
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)

plt.tight_layout()
plt.savefig('day3_composite_functions.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Composite functions saved")

print("\n✓ All Day 3 mathematical function plots generated successfully!")