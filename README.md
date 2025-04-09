
# Plant Health Monitor

The Plant Health Monitor is a Python-based project that utilizes sensor data to assess and monitor the health of plants. By collecting and analyzing environmental parameters, it provides insights to help maintain optimal growing conditions.

## Features

- **Data Collection**: Gathers real-time data from various environmental sensors.
- **Data Analysis**: Processes the collected data to evaluate plant health indicators.
- **Alerts and Notifications**: Sends alerts when environmental parameters fall outside optimal ranges.
- **Data Visualization**: Provides graphical representations of environmental trends over time.

## Requirements

- Python 3.x
- Required Python libraries:
  - `Adafruit_DHT`
  - `time`
  - `datetime`
  - `matplotlib`
  - `smtplib`
  - `email`

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/FrankieDan/Plant-Health-Monitor.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd Plant-Health-Monitor
   ```
3. **Install Required Libraries**:
   ```bash
   pip install matplotlib
   ```
   *Note*: The `Adafruit_DHT` library may require manual installation depending on your system. Refer to the [Adafruit DHT Sensor Library](https://github.com/adafruit/Adafruit_Python_DHT) for detailed instructions.

## Usage

1. **Configure Email Notifications**:
   - Open the `plant_health_monitor.py` file.
   - Locate the email configuration section:
     ```python
     sender_email = "your_email@example.com"
     receiver_email = "receiver_email@example.com"
     password = "your_email_password"
     ```
   - Replace the placeholder values with your actual email credentials to enable notification functionality.

2. **Run the Script**:
   ```bash
   python plant_health_monitor.py
   ```
   The script will begin collecting sensor data, analyzing it, and providing real-time feedback on plant health. Alerts will be sent via email if any environmental parameters are outside the optimal range.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
