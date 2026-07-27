import numpy as np

def runge_kutta(f, y0, t0, t_end, h):
    """
    Solve dy/dt = f(t, y) using the 4th Order Runge-Kutta Method.

    Parameters:
        f      : Differential equation function
        y0     : Initial value of y
        t0     : Initial time
        t_end  : Final time
        h      : Step size

    Returns:
        t_values : Time values
        y_values : Numerical solution
    """

    # Number of steps
    n_steps = int(round((t_end - t0) / h))

    # Arrays
    t_values = np.zeros(n_steps + 1)
    y_values = np.zeros(n_steps + 1)

    # Initial conditions
    t_values[0] = t0
    y_values[0] = y0

    # RK4 Loop
    for i in range(n_steps):

        t = t_values[i]
        y = y_values[i]

        k1 = h * f(t, y)

        k2 = h * f(t + h/2, y + k1/2)

        k3 = h * f(t + h/2, y + k2/2)

        k4 = h * f(t + h, y + k3)

        y_values[i + 1] = y + (k1 + 2*k2 + 2*k3 + k4) / 6

        t_values[i + 1] = t + h

    return t_values, y_values