import RPi.GPIO as GPIO ## Import GPIO library
import time

def ledOnOff(status):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, status)
