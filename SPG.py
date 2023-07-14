# Import necessary libraries for reading voltage data
import time
import random

# Simulating voltage readings (replace this code with your actual sensor or monitoring system code)
def get_voltage_reading():
    # Simulate a voltage reading between 100 and 250 volts
    voltage = random.uniform(100, 250)
    return voltage

# Function to check if voltage is low
def is_voltage_low(voltage, threshold):
    return voltage < threshold

# Main loop for continuous voltage monitoring
def monitor_voltage():
    threshold = 150  # Set your desired low voltage threshold in volts

    while True:
        voltage = get_voltage_reading()  # Replace this with your actual voltage reading code
        print("Current Voltage: %.2f V" % voltage)

        if is_voltage_low(voltage, threshold):
            print("Low Voltage Detected!")
            # Take appropriate action here, such as generating an alert or sending a notification

        time.sleep(1)  # Adjust the sleep duration as needed

# Start voltage monitoring
monitor_voltage()
