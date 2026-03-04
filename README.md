# rpi-stepper-motor-control

A multi-stage stepper motor control system using Raspberry Pi, progressing from basic GPIO control to wireless Bluetooth-based control.

This project demonstrates practical embedded systems implementation using Python and Raspberry Pi GPIO.

---

## 📌 Project Overview

This repository contains three progressive implementations of stepper motor control:

1. Basic GPIO motor control  
2. Direction control using a toggle switch  
3. Wireless Bluetooth control using BlueDot  

The project highlights modular design, hardware interfacing, and wireless communication techniques.

---

## 🧠 Hardware Used

- Raspberry Pi (BCM GPIO mode)
- 28BYJ-48 Stepper Motor
- ULN2003 Motor Driver
- Toggle Switch
- Android Smartphone (BlueDot App)

---

## ⚙️ Software Requirements

- Raspberry Pi OS
- Python 3
- RPi.GPIO library
- BlueDot library
- BlueZ (Linux Bluetooth stack)

---

## 📂 Project Structure

```
rpi-stepper-motor-control/
│
├── basic_gpio_control/
│   └── stepper_basic.py
│
├── toggle_switch_control/
│   └── stepper_toggle.py
│
└── bluetooth_control_bluedot/
    │   └── stepper_bluetooth.py
    │
    └── setup/
        └── bluetooth_setup.md
```

---

# 🚀 Stage 1 – Basic GPIO Control

- Implements half-step motor sequence
- Continuous forward rotation
- Speed control using delay timing
- Demonstrates GPIO output handling

Run:

```
python3 stepper_basic.py
```

---

# 🔁 Stage 2 – Toggle Switch Direction Control

- Hardware-based direction switching
- Forward / Reverse control using GPIO input
- Demonstrates external control logic

Run:

```
python3 stepper_toggle.py
```

---

# 📡 Stage 3 – Bluetooth Control (BlueDot)

- Wireless motor control via smartphone
- Command-based direction control
- Real-time forward / reverse / stop operation

Supported Commands:
```
forward
reverse
stop
```

Run:

```
python3 stepper_bluetooth.py
```

Bluetooth installation and setup instructions are available in:

```
bluetooth_control_bluedot/setup/bluetooth_setup.md
```

---

# 🎯 Key Concepts Demonstrated

- GPIO configuration using BCM mode
- Stepper motor half-step sequencing
- Direction control via sequence reversal
- Digital input handling
- Bluetooth communication using BlueDot
- Modular code organization
- Safe interrupt handling and GPIO cleanup

---

# 🔄 Communication Flow (Bluetooth Version)

Smartphone (BlueDot App)  
→ Bluetooth  
→ Raspberry Pi  
→ Python Script  
→ ULN2003 Driver  
→ Stepper Motor  

---

# 🛠 Future Improvements

- Speed control via Bluetooth
- Acceleration ramping
- Bluetooth Serial (RFCOMM) version
- Web-based motor control dashboard
- Closed-loop control using encoder feedback

---

# 👩‍💻 Author

Urmila Ghotekar  
Embedded Systems & IoT Enthusiast  

---

# 📜 License

This project is for educational and experimental purposes.
