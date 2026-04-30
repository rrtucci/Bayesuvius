import numpy as np
import matplotlib.pyplot as plt
from math import gamma, pi

def plot_laplacian_greens_fun():
    """
    This function plots the Green's function G(R) for minus the Laplacian for
    various dimensions d including some fractional ones

    -nabla^d G(R) = delta^d(R)

    Returns
    -------
    None

    """
    def G_fun(R, d):
        if abs(d - 2.0) < 1e-8:
            return (1/(2*pi)) * np.log(R)
        else:
            prefactor = gamma(d/2) / (2*(d-2)*(pi**(d/2)))
            return prefactor * R**(2-d)

    # R range (avoid R=0)
    R = np.linspace(0, 1,500)

    # dimensions to plot
    dims = [0.5, 1.0, 1.7, 2.3, 3.0]

    plt.figure()

    for d in dims:
        G_vals = G_fun(R, d)
        plt.plot(R, G_vals, label=f"d = {d}")

    # draw axes in black
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # labels and title
    plt.xlabel("R")
    plt.ylabel("G(R)")
    plt.title("Free-space Green's Function of Laplacian in Continuous Dimensions")

    # set y-axis limits
    plt.ylim(-1, 1)

    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    def main():
        plot_laplacian_greens_fun()

    main()