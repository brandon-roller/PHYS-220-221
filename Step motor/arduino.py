# Brandon Roller, Aldiyar Zhumashov


import serial
import time


class Arduino:
    """
    Class for connecting to and controlling the arduino
    """
    def __init__(self, port: str, baud: int, timeout: float):
        """
        Constructor, initializes serial communication
        :param port: Where to find the arduino
        :param baud: The bytes/second communication rate
        :param timeout: The timeout speed
        """
        self.arduino = serial.Serial(port=port, baudrate=baud, timeout=timeout)

    def await_response(self):
        """
        Helper method, waits for a signal from the arduino and prints the message
        """
        message = self.arduino.readline()
        while bytes("\n", "utf-8") not in message:
            time.sleep(0.1)
            message = self.arduino.readline()

        print(message)

    def step(self, s: int):
        """
        Steps the motor
        :param s: The desired number of steps
        """
        self.arduino.write(bytes(f"s {s}", "utf-8"))
        self.await_response()

    def read(self, pin: str):
        """
        Reads a voltage input and prints it out
        :param pin: The pin to read from
        """
        self.arduino.write(bytes(f"r {pin}", "utf-8"))
        self.await_response()


# Example usage
if __name__ == "__main__":

    ar = Arduino('/dev/cu.usbmodem101', 9600, 0.1)
    ar.step(10_000)
    ar.read("A0")
