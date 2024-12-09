# VPN Monitor
A lightweight tool to monitor VPN connection status, log events, and send notifications for disconnection or reconnection.

## Features
- Periodically checks VPN connection status.
- Logs events with timestamps.
- Sends desktop notifications on VPN disconnection or reconnection.

## Requirements
- Python 3.x
- Libraries: psutil, schedule, plyer

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the script:
   ```bash
   python main.py
   ```

## Usage
- Update `VPN_NAME` in `main.py` with your VPN's adapter name.
- The tool will check the connection status every 30 seconds.

## License
This project is licensed under the MIT License.
