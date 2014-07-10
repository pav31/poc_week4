import math
import matplotlib.pyplot as plt
import numpy as np


def f(n):
    """
    A test function
    """
    return 0.5 * n ** 2 - 5 * n + 20

def g(n):
    """
    A test function
    """
    # return n * math.log(n)
    # return 1
    return n ** 2
    # return n ** 3


def make_plot(fun1, fun2, plot_length):
    """
    Create a plot relating the growth of fun1 vs. fun2
    """
    x_plot, y_plot = [], []
    for index in range(2, plot_length):
        x_plot.append(index)
        y_plot.append(fun1(index) / float(fun2(index)))
    plt.plot(x_plot, y_plot)

    box = dict(facecolor='yellow', pad=5, alpha=0.7)

    plt.title("Growth rate comparison", bbox=box)
    plt.xlabel("n", bbox=box)
    plt.ylabel("f(n)/g(n)", bbox=box)

    plt.grid(True)
    plt.show()

# create an example plot
make_plot(f, g, 100)




