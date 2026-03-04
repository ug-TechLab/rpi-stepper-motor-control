"""
Project: Raspberry Pi Stepper Motor Control
Stage: Bluetooth Direction Control (BlueDot)
Motor: 28BYJ-48
Driver: ULN2003

Description:
This program controls stepper motor direction
using Bluetooth communication via BlueDot.

Commands:
"forward" -> Forward rotation
"reverse" -> Reverse rotation
"stop"    -> Stop motor
Press Ctrl+C to exit safely.
"""

import RPi.GPIO as GPIO
import time
from bluedot.btcomm import BluetoothServer

# ---------------- GPIO Setup ---------------- #

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Stepper motor pins
stepper_pins = [13, 16, 26, 21]
GPIO.setup(stepper_pins, GPIO.OUT)
GPIO.output(stepper_pins, GPIO.LOW)

# ---------------- Stepper Half-Step Sequence ---------------- #

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

# ---------------- Stepper Functions ---------------- #

def forward():
    for row in stepper_sequence:
        GPIO.output(stepper_pins, row)
        time.sleep(0.01)


def reverse():
    for row in reversed(stepper_sequence):
        GPIO.output(stepper_pins, row)
        time.sleep(0.01)


# ---------------- Bluetooth Handling ---------------- #

motor_direction = None  # Global state variable


def data_received(data):
    global motor_direction

    command = data.strip().lower()

    if command == "forward":
        motor_direction = "forward"
        print("Motor set to FORWARD")

    elif command == "reverse":
        motor_direction = "reverse"
        print("Motor set to REVERSE")

    elif command == "stop":
        motor_direction = None
        print("Motor STOPPED")

    else:
        print("Unknown command:", command)


# Start Bluetooth server
server = BluetoothServer(data_received)
print("Bluetooth server started. Waiting for connection...")

# ---------------- Main Loop ---------------- #

try:
    while True:

        if motor_direction == "forward":
            forward()

        elif motor_direction == "reverse":
            reverse()

        else:
            time.sleep(0.1)  # Idle wait

except KeyboardInterrupt:
    print("\nStopping program...")

finally:
    GPIO.cleanup()
    print("GPIO cleaned up successfully.")
