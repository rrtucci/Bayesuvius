import numpy as np
import matplotlib.pyplot as plt


def green_plus_green_minus_plots(s):
    """
    If N(x;s^2) is normal distribution with mean zero and
    standard deviation s, plot
    N(x-1;s^2)
    N(x+1;s^2)
    N(x-1;s^2)+ N(x+1;s^2)
    N(x-1;s^2)- N(x+1;s^2)


    Parameters
    ----------
    s: float
        standard deviation

    Returns
    -------

    """

    # Define normal distribution N(x; s_sq)
    def N(x, s_sq):
        a = 1 / np.sqrt(2 * np.pi * s_sq)
        return a * np.exp(-(x ** 2) / (2 * s_sq))

    # x range
    x = np.linspace(-5, 5, 1000)

    s_sq = s ** 2

    # Functions
    y1 = N(x - 1, s_sq)
    y2 = N(x + 1, s_sq)
    y_sum = y1 + y2
    y_diff = y1 - y2

    # Create figure
    plt.figure()

    # Plot curves
    plt.plot(x, y1, label="N(x-1; s^2)")
    plt.plot(x, y2, label="N(x+1; s^2)")
    plt.plot(x, y_sum, label="N(x-1; s^2) + N(x+1; s^2)")
    plt.plot(x, y_diff, label="N(x-1; s^2) - N(x+1; s^2)")

    # Draw black axes
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Labels and legend
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Gaussian Combinations with s = {s}")
    plt.legend()

    plt.show()


def green_pm_s1_s2_plots(s1, s2, sign):
    """
    If N(x;s^2) is normal distribution with mean zero and
    standard deviation s, plot
    N(x-1;s1^2) + sign* N(x+1;s1^2)
    N(x-1;s2^2) + sign* N(x+1;s2^2)


    Parameters
    ----------
    s1: float
        standard deviation
    s2: float
        standard deviation
    sign: int
        either +1 or -1
    Returns
    -------

    """

    # Define normal distribution N(x; s_sq)
    def N(x, s_sq):
        a = 1 / np.sqrt(2 * np.pi * s_sq)
        return a * np.exp(-(x ** 2) / (2 * s_sq))

    # x range
    x = np.linspace(-5, 5, 1000)

    s1_sq = s1 ** 2
    s2_sq = s2 ** 2

    # Functions
    y1 = N(x - 1, s1_sq) + sign * N(x + 1, s1_sq)
    y2 = N(x - 1, s2_sq) + sign * N(x + 1, s2_sq)

    # Create figure
    plt.figure()

    # Plot curves
    if sign == 1:
        sign_str = "+"
    elif sign == -1:
        sign_str = "-"
    else:
        assert False

    plt.plot(x, y1,
             label=f"N(x-1;s1^2) {sign_str} N(x+1;s1^2)")
    plt.plot(x, y2,
             label=f"N(x-1;s2^2) {sign_str} N(x+1;s2^2)")

    # Draw black axes
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Labels and legend
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Gaussian Combinations with s1 = {s1} and s2 = {s2}")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    def main1():
        green_plus_green_minus_plots(.5)
        green_plus_green_minus_plots(1)


    def main2():
        green_pm_s1_s2_plots(.5, 1, +1)
        green_pm_s1_s2_plots(.5, 1, -1)


    # main1()
    main2()
