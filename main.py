import schedule
import time
from vpn_checker import check_vpn_connection
from logger import log_event
from notifier import send_notification

VPN_NAME = "MyVPN"

def monitor_vpn():
    if check_vpn_connection(VPN_NAME):
        log_event(f"{VPN_NAME} is connected.")
    else:
        log_event(f"{VPN_NAME} is disconnected.")
        send_notification("VPN Disconnected", f"{VPN_NAME} has been disconnected.")

schedule.every(30).seconds.do(monitor_vpn)

if __name__ == "__main__":
    print("VPN Monitor is running...")
    while True:
        schedule.run_pending()
        time.sleep(1)
