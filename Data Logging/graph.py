import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the path to the Data Logging folder
data_folder = "Data Logging"
csv_file_path = os.path.join(data_folder, "sensor_data.csv")

# Check if the CSV file exists
if not os.path.exists(csv_file_path):
    print(f"Error: '{csv_file_path}' not found. Please ensure the data logging script has been run.")
    exit(1)

# Read the CSV file
try:
    data = pd.read_csv(csv_file_path)
    
    # Convert the 'Timestamp' column to numeric
    data['Timestamp'] = pd.to_numeric(data['Timestamp'], errors='coerce')
    
    # Drop rows with invalid timestamps (if any)
    data.dropna(subset=['Timestamp'], inplace=True)
    
    # Convert timestamp to seconds
    data['Timestamp'] = data['Timestamp'] / 1000  # Convert milliseconds to seconds
except Exception as e:
    print(f"Error reading or processing the CSV file: {e}")
    exit(1)

# Plot the data
plt.figure(figsize=(12, 8))

# Temperature
plt.subplot(2, 2, 1)  
plt.plot(data['Timestamp'], data['Temperature'], label='Temperature (°C)', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)

# Humidity
plt.subplot(2, 2, 2)  
plt.plot(data['Timestamp'], data['Humidity'], label='Humidity (%)', color='green')
plt.xlabel('Time (s)')
plt.ylabel('Humidity (%)')
plt.title('Humidity Over Time')
plt.grid(True)

# Air Quality (PPM)
plt.subplot(2, 2, 3)  
plt.plot(data['Timestamp'], data['Air Quality (PPM)'], label='Air Quality (PPM)', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Air Quality (PPM)')
plt.title('Air Quality (PPM) Over Time')
plt.grid(True)

# AQI Value
plt.subplot(2, 2, 4)  
plt.plot(data['Timestamp'], data['AQI'], label='AQI', color='red')
plt.xlabel('Time (s)')
plt.ylabel('AQI')
plt.title('AQI Over Time')
plt.grid(True)

# Display the Graph
plt.tight_layout()
plt.show()