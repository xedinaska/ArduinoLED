#!/usr/bin/python
import sys
from ArduinoLEDController import ArduinoLEDController

if sys.argv.__len__() > 1:
    arduinoController = ArduinoLEDController()
    arduinoController.handle(sys.argv[1])