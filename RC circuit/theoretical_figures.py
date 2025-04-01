
import matplotlib.pyplot as plt
import numpy as np
from random import random


def rc(t, R, C, V_in):

    return V_in * (1 - np.exp(-t/(R*C)))



if __name__ == "__main__":


    R = 1
    C = 1
    V_in = 1


    fig, ax = plt.subplots()

    points = np.arange(0, 8, 0.01)

    ax.plot(points, [rc(p, R, C, V_in) for p in points], color="red")
    ax.plot(points, [1]*len(points), "--")

    ax.set_xticks([R*C])
    ax.set_yticks([V_in])
    ax.set_xticklabels([r"$R\times C$"])
    ax.set_yticklabels(["$V_{in}$"])

    plt.ylim(0, V_in*2)
    plt.xlim(0, R*C*5)
    plt.xlabel("$t$")
    plt.ylabel("$V_C(t)$")


    plt.show()
