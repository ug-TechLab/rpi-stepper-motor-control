"""
Project: Raspberry Pi Stepper Motor Control
Stage: Toggle Switch Direction Control
Motor: 28BYJ-48 (4-phase)
Driver: ULN2003

Description:
This program controls stepper motor direction using
a hardware toggle switch.
Switch HIGH  -> Forward rotation
Switch LOW   -> Reverse rotation
Press Ctrl+C to stop safely.
"""

import RPi.GPIO as GPIO
import time

# ---------------- GPIO Setup ---------------- #

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Stepper motor pins (ULN2003 IN1–IN4)
stepper_pins = [13, 16, 26, 21]

# Toggle switch input pin
switch_pin = 20   # Change if needed


def setup():
    """Initialize GPIO pins."""
    for pin in stepper_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


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


def run_motor():
    """Control motor direction based on toggle switch."""
    try:
        while True:
            direction = GPIO.input(switch_pin)

            if direction == GPIO.HIGH:
                # Forward rotation
                for step in stepper_sequence:
                    GPIO.output(stepper_pins, step)
                    time.sleep(0.01)
            else:
                # Reverse rotation
                for step in reversed(stepper_sequence):
                    GPIO.output(stepper_pins, step)
                    time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nStopping motor...")

    finally:
        GPIO.cleanup()
        print("GPIO cleaned up successfully.")


# ---------------- Main Execution ---------------- #

if __name__ == "__main__":
    setup()
    run_motor()
