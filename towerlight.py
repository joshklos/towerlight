import serial


class TowerLight(object):
    def __init__(self, serial_port=None, baud_rate=9600):
        self.serialPort = serial.Serial(serial_port, baud_rate)

    def __send_command__(self, cmd):
        self.serialPort.write(bytes([cmd]))

    def __interpret_command__(self, mode, on, off, blink):
        if mode == "ON":
            self.__send_command__(on)
        elif mode == "OFF":
            self.__send_command__(off)
        elif mode == "BLINK":
            self.__send_command__(blink)

    def red(self, mode):
        self.__interpret_command__(mode, 0x11, 0x21, 0x41)

    def yellow(self, mode):
        self.__interpret_command__(mode, 0x12, 0x22, 0x42)

    def green(self, mode):
        self.__interpret_command__(mode, 0x14, 0x24, 0x44)

    def buzzer(self, mode):
        self.__interpret_command__(mode, 0x18, 0x28, 0x48)

    def clear_all(self):
        self.red("OFF")
        self.yellow("OFF")
        self.green("OFF")
        self.buzzer("OFF")

    def close_connection(self):
        self.serialPort.close()
