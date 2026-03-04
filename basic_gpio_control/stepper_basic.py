"""
Project: Raspberry Pi Stepper Motor Control
Stage: Basic GPIO Interfacing
Motor: 28BYJ-48 (4-phase)
Driver: ULN2003
Author: Urmila Ghotekar

Description:
This program rotates a 28BYJ-48 stepper motor continuously
in forward direction using half-step sequencing.
The motor is controlled using Raspberry Pi GPIO pins.
Press Ctrl+C to safely stop the motor.
"""

import RPi.GPIO as GPIO
import time

# ---------------- GPIO Setup ---------------- #

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# GPIO pins connected to ULN2003 IN1-IN4
stepper_pins = [13, 16, 26, 21]

for pin in stepper_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# ---------------- Half-Step Sequence ---------------- #

stepper_sequence = [
    [GPIO.HIGH, GPIO.LOW,  GPIO.LOW,  GPIO.LOW],
    [GPIO.HIGH, GPIO.HIGH, GPIO.LOW,  GPIO.LOW],
    [GPIO.LOW,  GPIO.HIGH, GPIO.LOW,  GPIO.LOW],
    [GPIO.LOW,  GPIO.HIGH, GPIO.HIGH, GPIO.LOW],
    [GPIO.LOW,  GPIO.LOW,  GPIO.HIGH, GPIO.LOW],
    [GPIO.LOW,  GPIO.LOW,  GPIO.HIGH, GPIO.HIGH],
    [GPIO.LOW,  GPIO.LOW,  GPIO.LOW,  GPIO.HIGH],
    [GPIO.HIGH, GPIO.LOW,  GPIO.LOW,  GPIO.HIGH]
]

# ---------------- Motor Rotation ---------------- #

try:
    while True:
        for step in stepper_sequence:
            GPIO.output(stepper_pins, step)
            time.sleep(0.01)   # Speed control delay

except KeyboardInterrupt:
    print("\nStopping motor...")

finally:
    GPIO.cleanup()
    print("GPIO cleaned up successfully.")
