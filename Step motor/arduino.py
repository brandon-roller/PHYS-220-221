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

    def get_response(self) -> str:
        """
        Helper method, waits for a signal from the arduino and returns the message
        :return: The string that the arduino outputs
        """
        message = self.arduino.readline()
        while bytes("\n", "utf-8") not in message:
            time.sleep(0.1)
            message = self.arduino.readline()

        return message.__str__()

    def step(self, s: int):
        """
        Steps the motor
        :param s: The desired number of steps
        """
        self.arduino.write(bytes(f"s {s}", "utf-8"))
        print(self.get_response())

    def write(self, duty_cycle: int):
        """
        Writes a PWM to pin ~9 with a given duty cycle
        :param duty_cycle: Integer 0-255, 0 for always off, 255 for always on
        """
        self.arduino.write(bytes(f"w {duty_cycle}", "utf-8"))
        print(self.get_response())

    def read(self, pin: str) -> float:
        """
        Reads a voltage input, parses it, and returns the voltage as a float
        :param pin: The pin to read from
        :return: The voltage reading by the arduino
        """
        self.arduino.write(bytes(f"r {pin}", "utf-8"))

        message = self.get_response()

        tokens = message.split("~ ")

        return float(tokens[1][0:4])


# Example usage
if __name__ == "__main__":

    ar = Arduino('/dev/cu.usbmodem101', 9600, 0.1)
    ar.step(10_000)
    ar.read("A0")
