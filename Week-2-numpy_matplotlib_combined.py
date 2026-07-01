
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

print("Generating NumPy + Matplotlib combined visualizations...")

# ==================== EIGENVALUES & EIGENVECTORS ====================
print("Computing and visualizing eigenvalues and eigenvectors...")

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Eigenvalues & Eigenvectors Visualization', fontsize=16, fontweight='bold')

# Example 1: Symmetric matrix
A = np.array([
    [4, 1],
    [1, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"\nMatrix A:\n{A}")
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")

# Visualize eigenvectors and their transformation
ax = axes[0]

# Original eigenvectors (unit vectors in the direction of eigenvectors)
for i in range(2):
    v = eigenvectors[:, i]
    lambda_i = eigenvalues[i]
    # Plot eigenvector
    ax.arrow(0, 0, v[0], v[1], head_width=0.1, head_length=0.1, 
            fc=f'C{i}', ec=f'C{i}', linewidth=2.5, label=f'v_{i+1} (λ={lambda_i:.2f})')
    # Plot transformed eigenvector (A @ v = lambda * v)
    Av = A @ v
    ax.arrow(0, 0, Av[0], Av[1], head_width=0.1, head_length=0.1,
            fc=f'C{i}', ec=f'C{i}', linewidth=2.5, linestyle='--', alpha=0.6)

# Plot a general vector and its transformation
theta = np.pi/6
general_v = np.array([np.cos(theta), np.sin(theta)])
Av_general = A @ general_v
ax.arrow(0, 0, general_v[0], general_v[1], head_width=0.1, head_length=0.1,
        fc='red', ec='red', linewidth=2, alpha=0.5, label='General vector')
ax.arrow(0, 0, Av_general[0], Av_general[1], head_width=0.1, head_length=0.1,
        fc='darkred', ec='darkred', linewidth=2, linestyle='--', alpha=0.5, label='A·vector')

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.set_title('Matrix A: Eigenvector Properties\n(Dashed = transformed)', fontsize=12, fontweight='bold')
ax.legend(fontsize=9, loc='upper left')
ax.set_facecolor('#f8f9fa')

# Example 2: Visualize transformation on grid of vectors
ax = axes[1]

# Create a grid of vectors
theta_grid = np.linspace(0, 2*np.pi, 20, endpoint=False)
for theta in theta_grid:
    v = np.array([np.cos(theta), np.sin(theta)])
    Av = A @ v
    
    # Original vector (lighter)
    ax.arrow(0, 0, v[0], v[1], head_width=0.08, head_length=0.08,
            fc='blue', ec='blue', linewidth=1, alpha=0.3)
    # Transformed vector (darker)
    ax.arrow(0, 0, Av[0], Av[1], head_width=0.08, head_length=0.08,
            fc='red', ec='red', linewidth=1.5, alpha=0.7)

# Highlight eigenvectors
for i in range(2):
    v = eigenvectors[:, i]
    lambda_i = eigenvalues[i]
    ax.arrow(0, 0, v[0], v[1], head_width=0.12, head_length=0.12,
            fc=f'C{i}', ec=f'C{i}', linewidth=3, label=f'Eigenvector {i+1} (λ={lambda_i:.2f})')

ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.5, 3.5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.set_title('Transformation of Vector Field\n(Blue→Red shows effect of matrix)', fontsize=12, fontweight='bold')
ax.legend(fontsize=9, loc='upper left')
ax.set_facecolor('#f8f9fa')

plt.tight_layout()
plt.savefig('day5_eigenvalues_eigenvectors.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Eigenvalues and eigenvectors visualization saved")

# ==================== MATRIX DECOMPOSITION VISUALIZATION ====================
print("Visualizing matrix decomposition...")

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('Matrix Decomposition & Properties - Day 5', fontsize=16, fontweight='bold')

# 1. Eigenvalue magnitude spectrum
ax = axes[0, 0]
matrices = {
    'A': A,
    'B': np.array([[3, 2], [2, 3]]),
    'C': np.array([[2, 0.5], [0.5, 1]]),
}

for name, M in matrices.items():
    evals, _ = np.linalg.eig(M)
    evals_sorted = np.sort(np.abs(evals))[::-1]
    ax.bar([name]*len(evals_sorted), evals_sorted, width=0.3, label=name, alpha=0.7)

ax.set_ylabel('Eigenvalue Magnitude', fontsize=11)
ax.set_title('Eigenvalue Spectra', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')
ax.set_facecolor('#f8f9fa')

# 2. Condition number across matrices
ax = axes[0, 1]
matrix_names = ['Identity', 'Well-conditioned', 'Ill-conditioned']
condition_numbers = [
    np.linalg.cond(np.eye(3)),
    np.linalg.cond(np.array([[3, 0.1], [0.1, 2]])),
    np.linalg.cond(np.array([[1, 1-1e-10], [1, 1]])),
]
colors_cond = ['green', 'orange', 'red']
bars = ax.bar(matrix_names, condition_numbers, color=colors_cond, alpha=0.7, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Condition Number', fontsize=11)
ax.set_yscale('log')
ax.set_title('Matrix Conditioning\n(Lower = Better)', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')
ax.set_facecolor('#f8f9fa')

# Add value labels
for bar, val in zip(bars, condition_numbers):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{val:.2e}', ha='center', va='bottom', fontsize=9, fontweight='bold')

# 3. Determinant heatmap
ax = axes[1, 0]
scales = np.linspace(0.5, 2.5, 20)
translations = np.linspace(-1, 1, 20)
det_matrix = np.zeros((len(scales), len(translations)))

for i, s in enumerate(scales):
    for j, t in enumerate(translations):
        M = np.array([[s, t], [t, s]])
        det_matrix[i, j] = np.linalg.det(M)

im = ax.imshow(det_matrix, cmap='RdBu_r', aspect='auto', 
               extent=[translations[0], translations[-1], scales[0], scales[-1]],
               origin='lower', interpolation='nearest')
ax.set_xlabel('Translation factor', fontsize=11)
ax.set_ylabel('Scale factor', fontsize=11)
ax.set_title('Determinant Heatmap', fontsize=12, fontweight='bold')
fig.colorbar(im, ax=ax, label='det(M)')

# 4. Norm comparison
ax = axes[1, 1]
matrices_norm = [
    ('Identity', np.eye(3)),
    ('Diagonal', np.diag([1, 2, 3])),
    ('Random', np.random.randn(3, 3)),
]

norm_types = ['Frobenius', 'Spectral', 'Nuclear']
x_pos = np.arange(len(matrices_norm))
width = 0.25

for i, norm_type in enumerate(norm_types):
    norms = []
    for name, M in matrices_norm:
        if norm_type == 'Frobenius':
            n = np.linalg.norm(M, 'fro')
        elif norm_type == 'Spectral':
            n = np.linalg.norm(M, 2)
        else:  # Nuclear
            U, S, Vt = np.linalg.svd(M)
            n = np.sum(S)
        norms.append(n)
    
    ax.bar(x_pos + i*width, norms, width, label=norm_type, alpha=0.8, edgecolor='black')

ax.set_ylabel('Norm Value', fontsize=11)
ax.set_title('Matrix Norms Comparison', fontsize=12, fontweight='bold')
ax.set_xticks(x_pos + width)
ax.set_xticklabels([name for name, _ in matrices_norm])
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis='y')
ax.set_facecolor('#f8f9fa')

plt.tight_layout()
plt.savefig('day5_matrix_decomposition.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Matrix decomposition visualization saved")

# ==================== SVD VISUALIZATION ====================
print("Visualizing Singular Value Decomposition...")

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle('Singular Value Decomposition (SVD) - Day 5', fontsize=16, fontweight='bold')

# Create a rank-deficient matrix
np.random.seed(42)
U = np.linalg.qr(np.random.randn(50, 10))[0]
S_true = np.array([5, 4, 3, 2, 1.5, 1, 0.5, 0.3, 0.2, 0.1])
Vt = np.linalg.qr(np.random.randn(20, 10))[0].T
M = U @ np.diag(S_true) @ Vt

# Perform SVD
U_svd, S_svd, Vt_svd = np.linalg.svd(M, full_matrices=False)

# Plot 1: Singular values
ax = axes[0]
ax.semilogy(range(1, len(S_svd)+1), S_svd, 'bo-', linewidth=2.5, markersize=8, label='Singular values')
ax.axvline(x=5, color='red', linestyle='--', linewidth=2, label='Effective rank=5')
ax.set_xlabel('Index', fontsize=11)
ax.set_ylabel('Singular Value (log scale)', fontsize=11)
ax.set_title('Singular Value Spectrum', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, which='both')
ax.legend(fontsize=10)
ax.set_facecolor('#f8f9fa')

# Plot 2: Cumulative explained variance
ax = axes[1]
cumsum_var = np.cumsum(S_svd**2) / np.sum(S_svd**2)
ax.plot(range(1, len(cumsum_var)+1), cumsum_var, 'go-', linewidth=2.5, markersize=8, label='Cumulative variance')
ax.axhline(y=0.95, color='red', linestyle='--', linewidth=2, label='95% threshold')
ax.fill_between(range(1, len(cumsum_var)+1), cumsum_var, alpha=0.3, color='green')
ax.set_xlabel('Number of components', fontsize=11)
ax.set_ylabel('Cumulative Explained Variance', fontsize=11)
ax.set_title('Variance Explained', fontsize=12, fontweight='bold')
ax.set_ylim([0, 1.05])
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10)
ax.set_facecolor('#f8f9fa')

# Plot 3: Reconstruction error with different ranks
ax = axes[2]
ranks = range(1, min(11, M.shape[1]+1))
reconstruction_errors = []

for r in ranks:
    M_reconstructed = U_svd[:, :r] @ np.diag(S_svd[:r]) @ Vt_svd[:r, :]
    error = np.linalg.norm(M - M_reconstructed, 'fro')
    reconstruction_errors.append(error)

ax.semilogy(ranks, reconstruction_errors, 'ro-', linewidth=2.5, markersize=8)
ax.set_xlabel('Rank of reconstruction', fontsize=11)
ax.set_ylabel('Frobenius Norm Error (log scale)', fontsize=11)
ax.set_title('Reconstruction Error vs Rank', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, which='both')
ax.set_facecolor('#f8f9fa')

plt.tight_layout()
plt.savefig('day5_svd_visualization.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ SVD visualization saved")

print("\n✓ All Day 5 NumPy + Matplotlib combined visualizations generated successfully!")