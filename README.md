# Fly Drone Controller

**Python toolkit for drone control -- MultiWii protocol, joystick, waypoints, neural networks, hover, computer vision (2014)**

> The Swiss Army knife of Daniel Dieser's drone research in Puerto Madryn, Patagonia.

---

## What Is This?

A comprehensive Python toolkit for controlling drones via the **MultiWii Serial Protocol (MSP)**. This is the companion computer software that ran on Raspberry Pi and laptops, communicating with MultiWii flight controllers to enable autonomous flight, computer vision, and early neural network experiments.

This project was the **bridge between hardware and AI** -- the place where Python met flight controllers, where PID loops met neural networks, and where computer vision met real-world navigation.

## Features

### Flight Control
- **MultiWii Serial Protocol** -- Full MSP implementation for reading sensors and sending commands
- **PID Controllers** -- Position, altitude, and heading hold with tunable gains
- **Joystick Control** -- UDP-based remote control from ground station
- **Waypoint Navigation** -- Autonomous multi-point flight paths

### AI and Vision
- **Neural Network Controller** (`mw-neural.py`) -- Experimental ML-based flight control using pyrenn
- **Computer Vision** (`modules/vision.py`) -- OpenCV color tracking for visual navigation and object following
- **Face Detection** -- Haar cascade face detection from drone camera
- **IMU Data Plotting** -- Real-time visualization of accelerometer and gyroscope data

### Sensors and Logging
- **DHT11/DHT22** -- Temperature and humidity monitoring during flight
- **PIR Sensor** -- Motion detection experiments
- **Flight Logger** -- CSV recording of all flight parameters
- **Servo Control** -- Camera gimbal and payload control

## Scripts

| Script | What It Does |
|--------|-------------|
| `mw-hover-controller.py` | PID-based autonomous hover using motion capture feedback |
| `mw-height-controller.py` | Altitude hold using sonar/barometer |
| `mw-neural.py` | Neural network flight controller -- ML meets drones |
| `mw-joystick.py` | Ground station joystick via UDP to MultiWii |
| `mw-waypoint.py` | Autonomous waypoint navigation |
| `mw-logdata.py` | Flight data black box recorder |
| `mw-simulink-controller.py` | Matlab/Simulink integration |
| `cli.py` | Command-line interface for drone operations |
| `flylab.py` | Laboratory experiment framework |
| `video.py` | Camera streaming and recording |
| `pir.py` | PIR motion sensor experiments |
| `servo.py` | Servo motor and gimbal control |
| `send-joystick.py` | Alternative joystick sender |
| `test-imu-plot.py` | Real-time IMU data visualization |

## Modules

| Module | Purpose |
|--------|---------|
| `modules/pyMultiwii.py` | MultiWii Serial Protocol -- reads attitude, RC, IMU; sends commands |
| `modules/vehicle.py` | Vehicle abstraction -- unified interface for different flight controllers |
| `modules/vision.py` | OpenCV color tracking -- visual servoing for drones |
| `modules/pyrenn.py` | Neural network library -- recurrent nets for flight control |
| `modules/utils.py` | PID controllers, low-pass filters, coordinate transforms |
| `modules/UDPserver.py` | Ground station communication layer |
| `modules/camera/rpi-opencv/` | Raspberry Pi OpenCV examples: color, face, motion, timelapse |

## Requirements

```
Python 2.7 / 3.x
pyserial
numpy
OpenCV (cv2)
pygame (for joystick)
matplotlib (for IMU plotting)
```

## Context in My Journey

This toolkit represents the convergence of everything I was experimenting with in 2014:

- **pyMultiwii.py** -- Understanding serial protocols (later: understanding network protocols)
- **PID controllers** -- Real-time feedback loops (later: active learning feedback loops in AI)
- **mw-neural.py** -- My first neural network controlling a physical system (later: neural networks classifying attacks)
- **vision.py** -- Computer vision on a flying platform (later: YOLOv3 fire detection, NDVI analysis)

The drone lab in Patagonia was where hardware, software, and AI first merged in my work. Everything I built after -- from JarvisIA to TokioAI -- has roots in this messy, experimental, beautiful codebase.

## Credits

Built on top of tools and libraries from the open-source drone community, including pyMultiwii by Aldo Vargas, pyrenn, and Adafruit sensor libraries. Extended with custom experiments in neural flight control and computer vision.

## License

GPL v3

---

*Daniel Dieser -- Puerto Madryn, Patagonia, Argentina*
*Telegram: [@mrmoz33](https://t.me/mrmoz33)*
