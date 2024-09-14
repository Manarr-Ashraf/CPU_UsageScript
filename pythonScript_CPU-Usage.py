# from gpiozero import LED
import psutil
from time import sleep
from datetime import datetime

# red_Led = LED()
# yellow_Led = LED()
# green_Led = LED()

myFile = open("log_file.txt","a")

try:
    while True:
    
        cpu_usage = psutil.cpu_percent(interval = 5, percpu = True)
        cpu_usage_mean = sum([i/len(cpu_usage) for i in cpu_usage])
        cpu_usage_mean = round(cpu_usage_mean, 3)
        print(f"cpu usage (%) : {cpu_usage_mean}%")

        # if cpu_usage_mean < 50:
        #     green_Led.on()
        #     red_Led.off()
        #     yellow_Led.off()
        # elif cpu_usage_mean < 80:
        #     green_Led.off()
        #     red_Led.off()
        #     yellow_Led.on()
        # elif cpu_usage_mean >= 80:
        #     green_Led.off()
        #     red_Led.on()
        #     yellow_Led.off()
        # else:
        #     green_Led.off()
        #     red_Led.off()
        #     yellow_Led.off()

        data = f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}" \
        f"cpu usage(%) : {cpu_usage_mean}% \n"
        myFile.write(data)
        sleep(1)
        
        
except KeyboardInterrupt:
        print("\nProgram stopped manually.")        
        
        