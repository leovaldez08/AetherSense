import serial
import time
import csv

def initialize_serial(port, baudrate):
    try:
        ser = serial.Serial(port, baudrate)
        print(f"Connected to {port} at {baudrate} baud.")
        return ser
    except serial.SerialException as e:
        print(f"Failed to connect to {port}: {e}")
        return None

port = 'COM10'  
baudrate = 9600
ser = None

while ser is None:
    ser = initialize_serial(port, baudrate)
    if ser is None:
        print("Retrying in 5 seconds...")
        time.sleep(5)

with open('sensor_data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature", "Humidity", "Air Quality (PPM)", "AQI"])  

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                data = line.split(',')
                writer.writerow(data) 
                print(f"Logged: {data}")
    except KeyboardInterrupt:
        print("Logging stopped.")
    finally:
        ser.close()