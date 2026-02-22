# Micro:bit Vehicle Black Box Simulator
Embedded Systems • Micro:bit • Python • Telemetry

Educational embedded system that simulates a vehicle telemetry recorder using the BBC Micro:bit.

## Demo

[![Microbit demo](https://gist.github.com/user-attachments/assets/cfe737df-6dd2-4356-ba91-7eccce8a7d71)](https://gist.github.com/user-attachments/assets/cfe737df-6dd2-4356-ba91-7eccce8a7d71
)

## Features

- Event-based telemetry recording
- Simulated vehicle metrics
- Circular memory buffer
- On-device playback interface

## Recorded Data

- Speed (0–80 km/h)
- Acceleration (-2 to 2 m/s²)
- Position (X,Y simplified)
- Timestamp

## Controls

Button A — Start / stop recording  
Button B — Show stored records  
Buttons A+B — Exit visualization

## Technical Notes

The system runs entirely on the Micro:bit and must operate under strict memory constraints.

- Maximum 20 stored records
- Oldest entries are overwritten automatically
- Lightweight data structures for embedded execution

## Possible Extensions

- Real sensor integration
- GPS module
- External storage
- Wireless telemetry
