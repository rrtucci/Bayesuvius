import numpy as np
import matplotlib.pyplot as plt


def green_plus_green_minus_plots(x):
    """
    Plot
    abs(x'-x)/2
    abs(x'+x)/2
    abs(x'-x)/2+ abs(x'+x)/2
    abs(x'-x)/2- abs(x'+x)/2


    Parameters
    ----------
    x: float
        source position

    Returns
    -------

    """
    xp = np.linspace(-5, 5, 1000)

    # Functions
    y1 = abs(xp-x)/2
    y2 = abs(xp+x)/2
    y_sum = y1 + y2
    y_diff = y1 - y2

    # Create figure
    plt.figure()

    # Plot curves
    plt.plot(xp, y1, label="abs(x'-x)/2")
    plt.plot(xp, y2, label="abs(x'+x)/2")
    plt.plot(xp, y_sum, label="abs(x'-x)/2 + abs(x'+x)/2")
    plt.plot(xp, y_diff, label="abs(x'-x)/2 - abs(x'+x)/2")

    # Draw black axes
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Labels and legend
    plt.xlabel("x'")
    plt.ylabel("y")
    plt.title(f"x = {x}")
    plt.legend()

    plt.show()




if __name__ == "__main__":
    def main1():
        green_plus_green_minus_plots(1)


    main1()

