# AetherSense: Smart Air Quality Monitoring System

AetherSense is an IoT-based air quality monitoring system that measures temperature, humidity, and air quality using an Arduino Uno and sensors like DHT11 and MQ135. The system logs data to a CSV file and provides real-time visualization of air quality metrics.

---

## Features
- **Real-Time Monitoring**: Measures temperature, humidity, and air quality (PPM and AQI).
- **Data Logging**: Logs sensor data to a CSV file for analysis.
- **Visualization**: Generates graphs to visualize trends in air quality metrics.
- **Alerts**: Uses LEDs and a buzzer to indicate air quality levels (Good, Moderate, Unhealthy).

---

## Hardware Requirements
- Arduino Uno
- DHT11 Sensor (Temperature and Humidity)
- MQ135 Sensor (Air Quality)
- 16x2 LCD with I2C
- LEDs (Green, Yellow, Red)
- Buzzer
- Breadboard and Jumper Wires

---

## Software Requirements
- Arduino IDE
- Python 3.x
- Libraries:
  - `pyserial` (for data logging)
  - `pandas` (for data processing)
  - `matplotlib` (for visualization)

---

## Setup Instructions

### 1. Arduino Setup
1. Connect the hardware components as per the circuit diagram.
2. Upload the `AetherSense.ino` sketch to the Arduino Uno using the Arduino IDE.
3. Open the Serial Monitor to verify that the Arduino is sending data.

### 2. Python Setup
1. Install the required Python libraries:
   ```bash
   pip install pyserial pandas matplotlib
Bam, rock and roll!

