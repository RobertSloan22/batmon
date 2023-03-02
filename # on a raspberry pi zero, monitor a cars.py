# on a raspberry pi zero, monitor a cars battery voltage and display it on a 5 x 3 inch screen

import os
import sys
import time
import csv
import subprocess
import RPi.GPIO as GPIO
from mcp3001 import MCP3001
from mcp3008 import MCP3008
from mcp3551 import MCP3551

# Path to pngview (raspidmx)
PNGVIEWPATH = "/home/pi/raspidmx/pngview"

# Path to icon set
ICONPATH = "icons/small"

# Show battery icon
ICON = 1

# Set red and green LEDs
LEDS = 0

# Icon location
ICONX = 460
ICONY = 5

# ADC type (MCP3001, MCP3008 or MCP3551)
ADC = "MCP3001"

# ADC channel to use (from 0 to 7, only relevant for MCP3008)
ADCCHANNEL = 0

# ADC SPI pins (BOARD numbering scheme)
SPIMISO = 38
SPIMOSI = 37
SPICLK = 40
SPICS = 36

# GPIO pins for good voltage and low voltage LEDs (BOARD numbering scheme)
GOODVOLTPIN = 18
LOWVOLTPIN = 16

# Fully charged voltage, voltage at the percentage steps and shutdown voltage
VOLT100 = 4.1
VOLT75 = 3.76
VOLT50 = 3.63
VOLT25 = 3.5
VOLT0 = 3.2

# Value (in ohms) of the lower resistor from the voltage divider, connected to the ground line (1 if no voltage divider)
LOWRESVAL = 10000

# Value (in ohms) of the higher resistor from the voltage divider, connected to the positive line (0 if no voltage divider) 
HIGHRESVAL = 10000

# ADC voltage reference (3.3V for Raspberry Pi)
ADCVREF = 3.3

# Refresh rate (s)

REFRESHRATE = 10

# Display debug messages
DEBUGMSG = 0

# Create CSV output
CSVOUT = 0

# Set GPIO mode
GPIO.setmode(GPIO.BOARD)

# Set GPIO pins
GPIO.setup(GOODVOLTPIN, GPIO.OUT)

GPIO.setup(LOWVOLTPIN, GPIO.OUT)

# Set ADC
if ADC == "MCP3001":
    adc = MCP3001(SPIMISO, SPIMOSI, SPICLK, SPICS)
elif ADC == "MCP3008":
    