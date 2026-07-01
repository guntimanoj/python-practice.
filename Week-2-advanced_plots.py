
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

print("Generating advanced visualizations...")

# ==================== 3D SURFACE PLOT ====================
print("Creating 3D surface plots...")
fig = plt.figure(figsize=(16, 5))

# 3D Surface 1: z = sin(x) * cos(y)
ax = fig.add_subplot(131, projection='3d')
x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(x, y)
Z1 = np.sin(X) * np.cos(Y)

surf1 = ax.plot_surface(X, Y, Z1, cmap='viridis', alpha=0.9, edgecolor='none')
ax.set_title('z = sin(x)·cos(y)', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(elev=25, azim=45)
fig.colorbar(surf1, ax=ax, pad=0.1, label='z value')

# 3D Surface 2: z = x^2 + y^2 (paraboloid)
ax = fig.add_subplot(132, projection='3d')
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z2 = X**2 + Y**2

surf2 = ax.plot_surface(X, Y, Z2, cmap='plasma', alpha=0.9, edgecolor='none')
ax.set_title('z = x² + y² (Paraboloid)', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(elev=30, azim=120)
fig.colorbar(surf2, ax=ax, pad=0.1, label='z value')

# 3D Surface 3: z = exp(-x^2 - y^2) (Gaussian)
ax = fig.add_subplot(133, projection='3d')
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z3 = np.exp(-X**2 - Y**2)

surf3 = ax.plot_surface(X, Y, Z3, cmap='coolwarm', alpha=0.9, edgecolor='none')
ax.set_title('z = e^(-x² - y²) (Gaussian)', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(elev=35, azim=60)
fig.colorbar(surf3, ax=ax, pad=0.1, label='z value')

plt.tight_layout()
plt.savefig('day4_3d_surface_plots.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ 3D surface plots saved")

# ==================== CONTOUR PLOTS ====================
print("Creating contour plots...")
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('Contour Plots - Day 4', fontsize=16, fontweight='bold')

x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)

# Contour 1: z = x^2 + y^2
ax = axes[0, 0]
Z = X**2 + Y**2
contour1 = ax.contour(X, Y, Z, levels=15, cmap='viridis', linewidths=1)
ax.clabel(contour1, inline=True, fontsize=8)
contourf1 = ax.contourf(X, Y, Z, levels=15, cmap='viridis', alpha=0.7)
ax.set_title('z = x² + y²', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.colorbar(contourf1, ax=ax, label='z')

# Contour 2: z = sin(x) * cos(y)
ax = axes[0, 1]
Z = np.sin(X) * np.cos(Y)
contour2 = ax.contour(X, Y, Z, levels=15, cmap='plasma', linewidths=1)
ax.clabel(contour2, inline=True, fontsize=8)
contourf2 = ax.contourf(X, Y, Z, levels=15, cmap='plasma', alpha=0.7)
ax.set_title('z = sin(x)·cos(y)', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.colorbar(contourf2, ax=ax, label='z')

# Contour 3: z = e^(-x^2 - y^2) with filled contours only
ax = axes[1, 0]
Z = np.exp(-X**2 - Y**2)
contourf3 = ax.contourf(X, Y, Z, levels=20, cmap='coolwarm')
ax.set_title('z = e^(-x² - y²) [Filled]', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.colorbar(contourf3, ax=ax, label='z')

# Contour 4: z = x*y - x^2 - y^2 (saddle point)
ax = axes[1, 1]
Z = X*Y - X**2 - Y**2
contour4 = ax.contour(X, Y, Z, levels=15, cmap='RdBu_r', linewidths=1)
ax.clabel(contour4, inline=True, fontsize=8)
contourf4 = ax.contourf(X, Y, Z, levels=15, cmap='RdBu_r', alpha=0.7)
ax.set_title('z = xy - x² - y² [Saddle]', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.colorbar(contourf4, ax=ax, label='z')

plt.tight_layout()
plt.savefig('day4_contour_plots.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Contour plots saved")

# ==================== HEATMAPS ====================
print("Creating heatmaps...")
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('Heatmaps and Matrix Visualization - Day 4', fontsize=16, fontweight='bold')

# Heatmap 1: Random data
ax = axes[0, 0]
data1 = np.random.randn(10, 10)
im1 = ax.imshow(data1, cmap='viridis', aspect='auto', interpolation='nearest')
ax.set_title('Random Gaussian Data', fontsize=12, fontweight='bold')
ax.set_xlabel('Columns')
ax.set_ylabel('Rows')
fig.colorbar(im1, ax=ax, label='Value')

# Heatmap 2: Correlation matrix (simulated)
ax = axes[0, 1]
cov_matrix = np.array([
    [1.0, 0.8, 0.3, -0.2],
    [0.8, 1.0, 0.5, 0.1],
    [0.3, 0.5, 1.0, 0.7],
    [-0.2, 0.1, 0.7, 1.0]
])
im2 = ax.imshow(cov_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
ax.set_xticks([0, 1, 2, 3])
ax.set_yticks([0, 1, 2, 3])
ax.set_xticklabels(['Var1', 'Var2', 'Var3', 'Var4'])
ax.set_yticklabels(['Var1', 'Var2', 'Var3', 'Var4'])
ax.set_title('Correlation Matrix', fontsize=12, fontweight='bold')

# Add text annotations
for i in range(4):
    for j in range(4):
        text = ax.text(j, i, f'{cov_matrix[i, j]:.2f}',
                      ha="center", va="center", color="black", fontsize=9, fontweight='bold')

fig.colorbar(im2, ax=ax, label='Correlation')

# Heatmap 3: 2D Gaussian distribution
ax = axes[1, 0]
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)
Z = np.exp(-X**2 - Y**2) * np.cos(2*X)
im3 = ax.imshow(Z, cmap='RdBu_r', extent=[-3, 3, -3, 3], origin='lower', aspect='auto')
ax.set_title('Modulated Gaussian', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.colorbar(im3, ax=ax, label='Intensity')

# Heatmap 4: Frequency matrix (simulated dataset stats)
ax = axes[1, 1]
freq_matrix = np.array([
    [150, 120, 80, 40],
    [110, 130, 95, 50],
    [70, 100, 140, 120],
    [30, 45, 110, 160]
])
im4 = ax.imshow(freq_matrix, cmap='YlOrRd', aspect='auto')
ax.set_xticks([0, 1, 2, 3])
ax.set_yticks([0, 1, 2, 3])
ax.set_xticklabels(['A', 'B', 'C', 'D'])
ax.set_yticklabels(['Group1', 'Group2', 'Group3', 'Group4'])
ax.set_title('Frequency Heatmap', fontsize=12, fontweight='bold')

# Add text annotations
for i in range(4):
    for j in range(4):
        text = ax.text(j, i, f'{freq_matrix[i, j]}',
                      ha="center", va="center", color="black", fontsize=9, fontweight='bold')

fig.colorbar(im4, ax=ax, label='Count')

plt.tight_layout()
plt.savefig('day4_heatmaps.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Heatmaps saved")

print("\n✓ All Day 4 advanced visualizations generated successfully!")