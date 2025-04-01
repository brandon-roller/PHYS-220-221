import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def root(x, v_0, w):
    return v_0 / np.sqrt(1+(w*x)**2)


def arc_tangent(x, w):
    return np.atan(w*x) * 180/np.pi


def compute_r_squared(func, xdata, ydata, *args):
    residuals = ydata - func(xdata, *args)
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

    figs = 1

    """Lock-in"""

    lock_in_data = np.loadtxt("lock-in_output.txt")

    frequency = lock_in_data[:, 0]
    amplitude = lock_in_data[:, 1]
    phase = lock_in_data[:, 2]

    # Lock in amplitude
    popt, pcov = curve_fit(root, frequency, amplitude, p0=(0.1, 1.0))
    phase_plot = plt.figure(figs)
    figs += 1
    plt.plot(frequency, root(frequency, *popt),
             label="Best fit: $\\frac{%s}{\\sqrt{1+(%s f)^2}}$" % tuple(scientific_notation(p) for p in popt))
    plt.scatter(frequency, amplitude, color="red", marker='.', label="Lock-in Data")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (V)")
    plt.title(f"Fit $R^2={compute_r_squared(root, frequency, amplitude, *popt): .5}$")
    plt.legend(fontsize=14)
    phase_plot.show()

    # Lock in phase
    popt, pcov = curve_fit(arc_tangent, frequency, phase, p0=(-0.5))
    phase_plot = plt.figure(figs)
    figs += 1
    plt.plot(frequency, arc_tangent(frequency, *popt),
             label="Best fit: $\\tan^{-1}(%s f)$" % tuple(scientific_notation(p) for p in popt))
    plt.scatter(frequency, phase, color="red", marker='.', label="Lock-in Data")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (Degree)")
    plt.title(f"Fit $R^2={compute_r_squared(arc_tangent, frequency, phase, *popt): .5}$")
    plt.legend(fontsize=14)
    phase_plot.show()

    # Lock in phase, first 3rd of data fit, ignore rest
    third_size = len(frequency) // 3

    popt, pcov = curve_fit(arc_tangent, frequency[0:third_size], phase[0:third_size], p0=(-0.5))
    phase_plot = plt.figure(figs)
    figs += 1
    plt.plot(frequency[0:third_size], arc_tangent(frequency[0:third_size], *popt),
             label="Best fit: $\\tan^{-1}(%s f)$" % tuple(scientific_notation(p) for p in popt))
    plt.scatter(frequency, phase, color="red", marker='.', label="Lock-in Data")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (Degree)")
    plt.title(f"Fit $R^2={compute_r_squared(arc_tangent, frequency[0:third_size], phase[0:third_size], *popt): .5}$")
    plt.legend(fontsize=14)
    phase_plot.show()

    """Oscilloscope"""

    oscilloscope_data = np.loadtxt("oscilloscope_output.txt")
    frequency = oscilloscope_data[:, 0]
    amplitude = oscilloscope_data[:, 1]
    phase = oscilloscope_data[:, 2]

    # Oscilloscope amplitude
    popt, pcov = curve_fit(root, frequency, amplitude, p0=(0.1, 1.0))
    amplitude_plot = plt.figure(figs)
    figs += 1
    plt.plot(frequency, root(frequency, *popt),
             label="Best fit: $\\frac{%s}{\\sqrt{1+(%s f)^2}}$" % tuple(scientific_notation(p) for p in popt))
    plt.scatter(frequency, amplitude, color="red", marker='.', label="Oscilloscope Data")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (V)")
    plt.title(f"Fit $R^2={compute_r_squared(root, frequency, amplitude, *popt): .5}$")
    plt.legend(fontsize=14)
    amplitude_plot.show()

    # Oscilloscope phase
    popt, pcov = curve_fit(arc_tangent, frequency, phase, p0=(-0.5))
    phase_plot = plt.figure(figs)
    figs += 1
    plt.plot(frequency, arc_tangent(frequency, *popt),
             label="Best fit: $\\tan^{-1}(%s f)$" % tuple(scientific_notation(p) for p in popt))
    plt.scatter(frequency, phase, color="red", marker='.', label="Oscilloscope Data")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (Degree)")
    plt.title(f"Fit $R^2={compute_r_squared(arc_tangent, frequency, phase, *popt): .5}$")
    plt.legend(fontsize=14)
    phase_plot.show()

    """Oscilloscope phase data cleaned"""

    oscilloscope_data = np.loadtxt("cleaned_oscilloscope_data.txt")
    frequency = oscilloscope_data[:, 0]
    phase = oscilloscope_data[:, 2]

    # Cleaned oscilloscope phase
    popt, pcov = curve_fit(arc_tangent, frequency, phase, p0=(-0.5))
    phase_plot = plt.figure(figs)
    figs += 1
    plt.plot(frequency, arc_tangent(frequency, *popt),
             label="Best fit: $\\tan^{-1}(%s f)$" % tuple(scientific_notation(p) for p in popt))
    plt.scatter(frequency, phase, color="red", marker='.', label="Oscilloscope Data, cleaned")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (Degree)")
    plt.title(f"Fit $R^2={compute_r_squared(arc_tangent, frequency, phase, *popt): .5}$")
    plt.legend(fontsize=14)
    phase_plot.show()

    # Cleaned oscilloscope phase, first third fit

    third_size = len(frequency) // 3

    popt, pcov = curve_fit(arc_tangent, frequency[0:third_size], phase[0:third_size], p0=(-0.5))
    phase_plot = plt.figure(figs)
    figs += 1
    plt.plot(frequency[0:third_size], arc_tangent(frequency[0:third_size], *popt),
             label="Best fit: $\\tan^{-1}(%s f)$" % tuple(scientific_notation(p) for p in popt))
    plt.scatter(frequency, phase, color="red", marker='.', label="Oscilloscope Data, cleaned")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (Degree)")
    plt.title(f"Fit $R^2={compute_r_squared(arc_tangent, frequency[0:third_size], phase[0:third_size], *popt): .5}$")
    plt.legend(fontsize=14)
    phase_plot.show()

    plt.show()
