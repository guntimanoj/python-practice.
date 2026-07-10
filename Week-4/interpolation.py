""
 SciPy Interpolation
Covers: interp1d, CubicSpline, PchipInterpolator, 2D interpolation (griddata)
"""

import numpy as np
from scipy.interpolate import interp1d, CubicSpline, PchipInterpolator, griddata
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# 1. Linear & Cubic interpolation with interp1d
# ---------------------------------------------------------
def demo_interp1d():
    x = np.linspace(0, 10, 10)
    y = np.sin(x)

    x_dense = np.linspace(0, 10, 200)

    f_linear = interp1d(x, y, kind="linear")
    f_cubic = interp1d(x, y, kind="cubic")

    y_linear = f_linear(x_dense)
    y_cubic = f_cubic(x_dense)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, "o", label="Data points")
    plt.plot(x_dense, y_linear, "--", label="Linear interp")
    plt.plot(x_dense, y_cubic, "-", label="Cubic interp")
    plt.plot(x_dense, np.sin(x_dense), ":", label="True sin(x)")
    plt.legend()
    plt.title("interp1d: Linear vs Cubic")
    plt.savefig("interp1d_demo.png", dpi=120)
    plt.close()

    print("interp1d results at x=4.5:")
    print(f"  linear -> {f_linear(4.5):.4f}")
    print(f"  cubic  -> {f_cubic(4.5):.4f}")
    print(f"  true   -> {np.sin(4.5):.4f}\n")


# ---------------------------------------------------------
# 2. Smooth interpolation with CubicSpline
# ---------------------------------------------------------
def demo_cubic_spline():
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0])

    cs = CubicSpline(x, y)
    x_dense = np.linspace(0, 5, 200)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, "o", label="Data points")
    plt.plot(x_dense, cs(x_dense), label="CubicSpline")
    plt.plot(x_dense, cs(x_dense, 1), "--", label="1st derivative")
    plt.legend()
    plt.title("CubicSpline: value + derivative")
    plt.savefig("cubic_spline_demo.png", dpi=120)
    plt.close()

    print("CubicSpline value and derivative at x=2.5:")
    print(f"  value      -> {cs(2.5):.4f}")
    print(f"  derivative -> {cs(2.5, 1):.4f}\n")


# ---------------------------------------------------------
# 3. Shape-preserving interpolation with PchipInterpolator
#    (avoids overshoot that CubicSpline can introduce)
# ---------------------------------------------------------
def demo_pchip():
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 1, 1, 0])  # flat region -> cubic spline overshoots

    cs = CubicSpline(x, y)
    pchip = PchipInterpolator(x, y)
    x_dense = np.linspace(0, 4, 200)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, "o", label="Data points")
    plt.plot(x_dense, cs(x_dense), "--", label="CubicSpline (overshoots)")
    plt.plot(x_dense, pchip(x_dense), label="PCHIP (shape-preserving)")
    plt.legend()
    plt.title("CubicSpline vs PCHIP on flat data")
    plt.savefig("pchip_demo.png", dpi=120)
    plt.close()
    print("PCHIP demo saved (compare overshoot vs shape-preserving fit)\n")


# ---------------------------------------------------------
# 4. 2D interpolation with griddata (scattered data -> grid)
# ---------------------------------------------------------
def demo_griddata():
    rng = np.random.default_rng(42)
    points = rng.uniform(-5, 5, size=(200, 2))
    values = np.sin(points[:, 0]) * np.cos(points[:, 1])

    grid_x, grid_y = np.mgrid[-5:5:100j, -5:5:100j]
    grid_z = griddata(points, values, (grid_x, grid_y), method="cubic")

    plt.figure(figsize=(6, 5))
    plt.imshow(grid_z.T, extent=(-5, 5, -5, 5), origin="lower", cmap="viridis")
    plt.scatter(points[:, 0], points[:, 1], c="white", s=5, alpha=0.4)
    plt.colorbar(label="interpolated value")
    plt.title("griddata: scattered 2D interpolation")
    plt.savefig("griddata_demo.png", dpi=120)
    plt.close()
    print("griddata demo saved (2D scattered-data interpolation)\n")


if __name__ == "__main__":
    demo_interp1d()
    demo_cubic_spline()
    demo_pchip()
    demo_griddata()
    print("All interpolation demos complete. PNG plots saved in this folder.")