import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def exponential(x, a, b, c, d):
    return a*np.exp(b*x+c)+d


def compute_r_squared(xdata, ydata, *args):
    residuals = ydata - exponential(xdata, *args)
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((ydata - np.mean(ydata)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    return r_squared


def scientific_notation(f: float) -> str:

    string = f"{f:.3E}"
    split = string.split("E")
    if int(split[1]) == 0:
        return split[0]
    else:
        return split[0] + "\\times10^{" + str(int(split[1])) + "}"


if __name__ == "__main__":

    """Lock-in"""

    lock_in_data = np.loadtxt("lock-in_output.txt")

    frequency = lock_in_data[:, 0]
    amplitude = lock_in_data[:, 1]
    phase = lock_in_data[:, 2]

    # Lock-in amplitude
    popt, pcov = curve_fit(exponential, frequency, amplitude, p0=(1.233, -4.904e-4, -9.519e-1, 6.138e-2))
    amplitude_plot = plt.figure(1)
    plt.plot(frequency, exponential(frequency, *popt),
             label="Best fit: $%s e^{%s f %s} + %s$" % tuple(scientific_notation(p) for p in popt))
    plt.scatter(frequency, amplitude, color="red", marker='.', label="Lock-in Data")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (V)")
    plt.title(f"Fit $R^2={compute_r_squared(frequency, amplitude, *popt): .3}$")
    plt.legend()
    amplitude_plot.show()

    # Lock-in phase
    popt, pcov = curve_fit(exponential, frequency, phase, p0=(2.437, -7.408e-4, 3.444, -77.119))
    phase_plot = plt.figure(2)
    plt.plot(frequency, exponential(frequency, *popt),
             label="Best fit: $%s e^{%s f-%s} %s$" % tuple(scientific_notation(p) for p in popt))
    plt.scatter(frequency, phase, color="red", marker='.', label="Lock-in Data")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (Degree)")
    plt.title(f"Fit $R^2={compute_r_squared(frequency, phase, *popt): .3}$")
    plt.legend()
    phase_plot.show()

    """Oscilloscope"""

    oscilloscope_data = np.loadtxt("oscilloscope_output.txt")
    frequency = oscilloscope_data[:, 0]
    amplitude = oscilloscope_data[:, 1]
    phase = oscilloscope_data[:, 2]

    # Oscilloscope amplitude
    popt, pcov = curve_fit(exponential, frequency, amplitude, p0=(1, -4.904e-4, 1, 0))
    amplitude_plot = plt.figure(3)
    plt.plot(frequency, exponential(frequency, *popt),
             label="Best fit: $%s e^{%s f %s} + %s$" % tuple(scientific_notation(p) for p in popt))
    plt.scatter(frequency, amplitude, color="red", marker='.', label="Oscilloscope Data")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (V)")
    plt.title(f"Fit $R^2={compute_r_squared(frequency, amplitude, *popt): .3}$")
    plt.legend()
    amplitude_plot.show()

    # Oscilloscope phase
    popt, pcov = curve_fit(exponential, frequency, phase, p0=(2.437, -7.408e-4, 3.444, -77.119))
    phase_plot = plt.figure(4)
    plt.plot(frequency, exponential(frequency, *popt),
             label="Best fit: $%s e^{%s f + %s} %s$" % tuple(scientific_notation(p) for p in popt))
    plt.scatter(frequency, phase, color="red", marker='.', label="Oscilloscope Data")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (Degree)")
    plt.title(f"Fit $R^2={compute_r_squared(frequency, phase, *popt): .3}$")
    plt.legend()
    phase_plot.show()

    """Oscilloscope phase data cleaned"""

    oscilloscope_data = np.loadtxt("cleaned_oscilloscope_data.txt")
    frequency = oscilloscope_data[:, 0]
    phase = oscilloscope_data[:, 2]

    # Cleaned oscilloscope phase
    popt, pcov = curve_fit(exponential, frequency, phase, p0=(2.437, -7.408e-4, 3.444, -77.119))
    phase_plot = plt.figure(5)
    plt.plot(frequency, exponential(frequency, *popt),
             label="Best fit: $%s e^{%s f +%s} %s$" % tuple(scientific_notation(p) for p in popt))
    plt.scatter(frequency, phase, color="red", marker='.', label="Oscilloscope Data, Bad Points Removed")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (Degree)")
    plt.title(f"Fit $R^2={compute_r_squared(frequency, phase, *popt): .3}$")
    plt.legend()
    phase_plot.show()

    plt.show()
