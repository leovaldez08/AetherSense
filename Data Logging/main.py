import serial
import time
import csv
import os

# Set up serial connection
ser = serial.Serial('COM10', 9600, timeout=1)  # Adjust COM port
ser.flushInput()  # Clear the input buffer

# Define the path to the Data Logging folder
data_folder = "Data Logging"
csv_file_path = os.path.join(data_folder, "sensor_data.csv")

# Create the Data Logging folder if it doesn't exist
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Check if the CSV file exists
file_exists = os.path.exists(csv_file_path)

# Open the CSV file to save data
with open(csv_file_path, 'a', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header only if the file is being created for the first time
    if not file_exists:
        writer.writerow(["Timestamp", "Temperature", "Humidity", "Air Quality (PPM)", "AQI"])

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                if line:  # Ensure the line is not empty
                    data = line.split(',')
                    if len(data) == 5:  # Ensure the data has 5 columns
                        writer.writerow(data)  # Write data to CSV
                        print(f"Logged: {data}")
    except KeyboardInterrupt:
        print("Logging stopped.")
    finally:
        ser.close()