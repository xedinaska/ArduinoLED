import time
import serial


class ArduinoLEDController:

    arduino = None

    def __init__(self):
        port = '/dev/tty.usbmodem1411'
        self.arduino = serial.Serial(port, 9600, timeout=5)
        time.sleep(2)

    def handle(self, param):
        colors = {'red': '1', 'green': '2', 'blue': '3', 'yellow': '4', 'pink': '5', 'violet': '6'}

        if param not in colors:
            color = '0'
        else:
            color = colors[param]

        self.arduino.write(str.encode(color))
