#!/usr/bin/python
import sys
from LEDController import ArduinoLEDController

if sys.argv.__len__() > 1:
    arduinoController = ArduinoLEDController.ArduinoLEDController()
    arduinoController.handle(sys.argv[1])