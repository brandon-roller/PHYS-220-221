# Brandon Roller, Aldiyar Zhumashov

from arduino import Arduino
from time import sleep

if __name__ == "__main__":

    ar = Arduino('/dev/cu.usbmodem101', 9600, 0.1)

    with open("output.txt", "w") as file:

        file.write("%-10s%-10s%-10s\n" % ("v1", "v2", "v3"))

        for v in range(0, 256):

            ar.write(v)
            sleep(0.3)  # Give the system time to react
            v1 = ar.read("1")
            v2 = ar.read("2")
            v3 = ar.read("3")
            file.write("%-10f%-10f%-10f\n" % (v1, v2, v3))
