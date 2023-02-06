# 设置你想要得到通知的电池百分比
# pip instal plyer
from plyer import notification
import psutil
from time import sleep
while True:
    battery = psutil.sensors_battery()
    life = battery.percent
    if life < 50:
        notification.notify(
            title = "Battery Low",
            message = "Please connect to power source",
            timeout = 10
        )
    sleep(60)