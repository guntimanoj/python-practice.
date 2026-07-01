
import matplotlib.pyplot as plt
import numpy as np

# ==================== LINE PLOT ====================
print("Generating line plots...")
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y1, label='sin(x)', linewidth=2, color='blue')
ax.plot(x, y2, label='cos(x)', linewidth=2, color='red', linestyle='--')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Trigonometric Functions', fontsize=14, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
plt.savefig('day1_line_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Line plot saved as day1_line_plot.png")

# ==================== BAR CHART ====================
print("Generating bar chart...")
categories = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
popularity = [95, 70, 65, 90, 45]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, popularity, color=colors, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Popularity Score', fontsize=12)
ax.set_title('Programming Language Popularity', fontsize=14, fontweight='bold')
ax.set_ylim(0, 100)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.savefig('day1_bar_chart.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Bar chart saved as day1_bar_chart.png")

# ==================== SCATTER PLOT ====================
print("Generating scatter plot...")
np.random.seed(42)
n_points = 100
x_scatter = np.random.randn(n_points) * 2
y_scatter = 2.5 * x_scatter + np.random.randn(n_points) * 3
colors_scatter = np.abs(x_scatter) * 10

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(x_scatter, y_scatter, c=colors_scatter, cmap='viridis', 
                     s=100, alpha=0.6, edgecolors='black', linewidth=0.5)
ax.set_xlabel('Feature X', fontsize=12)
ax.set_ylabel('Feature Y', fontsize=12)
ax.set_title('Scatter Plot with Color Mapping', fontsize=14, fontweight='bold')
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Intensity', fontsize=10)
ax.grid(True, alpha=0.3)
plt.savefig('day1_scatter_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Scatter plot saved as day1_scatter_plot.png")

print("\n✓ All Day 1 plots generated successfully!")