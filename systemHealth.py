import psutil
import time
from colorama import Fore,Style

# Infinite loop to continuously monitor CPU usage
while True:
    # Get CPU usage percentage over a 1-second interval
    cpu = psutil.cpu_percent(interval=1)
    
    # Display CPU usage with color coding:
    if cpu < 50:
        # Green for low CPU usage
        print(Fore.GREEN + f"🟢 CPU usage: {cpu}% 🍃"+ Style.RESET_ALL)
    elif cpu < 80:
        # Yellow for mederate CPU usage
        print(Fore.YELLOW + f"🟡 CPU usage: {cpu}% ⚖️" + Style.RESET_ALL)
    else:
        # Red for high CPU usage
        print(Fore.RED + f"🔴 CPU usage: {cpu}% 🚨"+ Style.RESET_ALL)
