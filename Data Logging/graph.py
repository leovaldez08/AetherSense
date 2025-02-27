import pandas as pd
import matplotlib.pyplot as plt

try:
    data = pd.read_csv('sensor_data.csv')
except FileNotFoundError:
    print("Error: 'sensor_data.csv' not found. Please ensure the data logging script has been run.")
    exit(1)

data['Timestamp'] = pd.to_numeric(data['Timestamp'], errors='coerce')
data.dropna(subset=['Timestamp'], inplace=True)
data['Timestamp'] = data['Timestamp'] / 1000  

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
plt.ylabel('Impurity Level (PPM)')
plt.title('Impure Substances level (PPM) Over Time')
plt.grid(True)

# AQI
plt.subplot(2, 2, 4)  
plt.plot(data['Timestamp'], data['AQI'], label='AQI', color='red')
plt.xlabel('Time (s)')
plt.ylabel('AQ ')
plt.title('AQI Value Over Time')
plt.grid(True)

plt.tight_layout()
plt.show()