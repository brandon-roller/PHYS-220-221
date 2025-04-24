import matplotlib.pyplot as plt
import numpy as np


def read(filename):

    array = [[], [], []]

    with open(filename) as file:
        lines = file.readlines()
        for line in lines[1:]:
            tokens = line.split("  ")
            array[0].append(float(tokens[0]))
            array[1].append(float(tokens[1]))
            array[2].append(float(tokens[2]))

    return array


if __name__ == "__main__":
    data = read("output.txt")

    analog_values = list(range(0, 256))

    plt.xlabel("PWM Duty Cycle (0-255)")
    plt.ylabel("Voltage $(V)$")

    plt.plot(analog_values, data[0], label="v1")
    plt.plot(analog_values, data[1], label="v2")
    plt.plot(analog_values, data[2], label="v3")

    plt.legend()
    plt.show()
