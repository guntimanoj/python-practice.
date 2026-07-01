
import matplotlib.pyplot as plt
import numpy as np

print("Generating subplots with styling...")

# ==================== MULTIPLE SUBPLOTS (2x2) ====================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Week 2 Day 2: Subplots and Styling', fontsize=16, fontweight='bold')

# Subplot 1: Line plot with multiple styles
x = np.linspace(0, 2*np.pi, 100)
ax = axes[0, 0]
ax.plot(x, np.sin(x), label='sin(x)', linewidth=2.5, color='#e74c3c', linestyle='-', marker='o', markersize=4, markevery=10)
ax.plot(x, np.cos(x), label='cos(x)', linewidth=2.5, color='#3498db', linestyle='--', marker='s', markersize=4, markevery=10)
ax.set_title('Trigonometric Functions', fontsize=12, fontweight='bold')
ax.set_xlabel('Radians', fontsize=10)
ax.set_ylabel('Value', fontsize=10)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.4, linestyle=':', linewidth=0.8)
ax.set_facecolor('#f8f9fa')

# Subplot 2: Exponential functions
ax = axes[0, 1]
x_exp = np.linspace(0, 3, 100)
ax.plot(x_exp, np.exp(x_exp), label='e^x', linewidth=2.5, color='#27ae60')
ax.plot(x_exp, 2**x_exp, label='2^x', linewidth=2.5, color='#f39c12', linestyle='--')
ax.fill_between(x_exp, np.exp(x_exp), alpha=0.3, color='#27ae60')
ax.set_title('Exponential Growth', fontsize=12, fontweight='bold')
ax.set_xlabel('x', fontsize=10)
ax.set_ylabel('y', fontsize=10)
ax.legend(loc='upper left', fontsize=9)
ax.set_yscale('log')
ax.grid(True, alpha=0.4, which='both', linestyle=':')
ax.set_facecolor('#f8f9fa')

# Subplot 3: Bar chart with error bars
ax = axes[1, 0]
categories = ['Q1', 'Q2', 'Q3', 'Q4']
values = [65, 78, 82, 88]
errors = [3, 4, 5, 3]
bars = ax.bar(categories, values, yerr=errors, capsize=8, 
              color=['#e74c3c', '#3498db', '#2ecc71', '#f39c12'],
              edgecolor='black', linewidth=1.5, error_kw={'linewidth': 2})
ax.set_title('Quarterly Performance', fontsize=12, fontweight='bold')
ax.set_ylabel('Score', fontsize=10)
ax.set_ylim(0, 100)
ax.grid(True, alpha=0.3, axis='y')
ax.set_facecolor('#f8f9fa')

# Add value labels
for i, (bar, val) in enumerate(zip(bars, values)):
    ax.text(bar.get_x() + bar.get_width()/2, val + errors[i] + 2,
            f'{val}', ha='center', va='bottom', fontsize=9, fontweight='bold')

# Subplot 4: Multiple scatter plots
ax = axes[1, 1]
np.random.seed(42)
for i, color in enumerate(['#e74c3c', '#3498db', '#2ecc71']):
    x_scatter = np.random.randn(30) + i
    y_scatter = np.random.randn(30) + i
    ax.scatter(x_scatter, y_scatter, label=f'Class {i+1}', 
              color=color, s=80, alpha=0.6, edgecolors='black', linewidth=0.5)

ax.set_title('Multi-class Scatter', fontsize=12, fontweight='bold')
ax.set_xlabel('Feature 1', fontsize=10)
ax.set_ylabel('Feature 2', fontsize=10)
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_facecolor('#f8f9fa')

plt.tight_layout()
plt.savefig('day2_subplots_styling.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Subplots with styling saved as day2_subplots_styling.png")

# ==================== LEGEND VARIATIONS ====================
print("Generating legend variations...")
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle('Legend Positioning and Styles', fontsize=14, fontweight='bold')

x = np.linspace(0, 10, 100)

for idx, (ax, loc) in enumerate(zip(axes, ['upper left', 'center right', 'lower center'])):
    ax.plot(x, np.sin(x), label='sin(x)', linewidth=2, marker='o', markersize=4, markevery=10)
    ax.plot(x, np.cos(x), label='cos(x)', linewidth=2, marker='s', markersize=4, markevery=10)
    ax.plot(x, np.tan(x/2), label='tan(x/2)', linewidth=2, marker='^', markersize=4, markevery=10)
    
    ax.set_title(f'Legend: {loc}', fontsize=11)
    ax.set_xlabel('x', fontsize=10)
    ax.set_ylabel('y', fontsize=10)
    ax.legend(loc=loc, fontsize=9, framealpha=0.95, edgecolor='black')
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#f8f9fa')
    ax.set_ylim(-3, 3)

plt.tight_layout()
plt.savefig('day2_legend_variations.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Legend variations saved as day2_legend_variations.png")

print("\n✓ All Day 2 plots generated successfully!")