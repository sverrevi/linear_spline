import matplotlib.pyplot as plt
import numpy as np
from interp import interp

def main():
    x = 3*np.pi
    xp = np.linspace(0, 2*np.pi, 500)
    yp = np.sin(xp)
    y_evaluated = interp(x, xp, yp)
    x_vals = [x, xp[-1]]
    y_vals = [y_evaluated, yp[-1]]
    plt.subplot(3, 1, 1)
    plt.plot(x, y_evaluated, "x")
    plt.plot(xp, yp, 'k')
    plt.plot(x_vals, y_vals, "--", color="k")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Case with constant extrapolation (right side) for sin(x)")

    x2 = 4
    xp2 = [1, 3, 5]
    yp2 = [4, 2, 1]
    y2_evaluated = interp(x2, xp2, yp2)
    plt.subplot(3, 1, 2)
    plt.plot(x2, y2_evaluated, "x")
    plt.plot(xp2, yp2,"-o", color="k")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Case with linear interpolation for dataset")

    x3 = -5
    xp3 = np.linspace(0, 3, 500)
    yp3 = np.exp(xp)
    y3_evaluated = interp(x3, xp3, yp3)
    x_vals3 = [x3, xp3[0]]
    y_vals3 = [y3_evaluated, yp3[0]]
    plt.subplot(3, 1, 3)
    plt.plot(x3, y3_evaluated, "x")
    plt.plot(xp3, yp3, "k")
    plt.plot(x_vals3, y_vals3, "--", color="k")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Case with constant extrapolation (left side) for exp(x)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()