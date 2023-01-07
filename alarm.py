from datetime import datetime
from playsound import playsound
alarm_time = input("Enter a time for alarm with this format (HH:MM:SS)")
alarm_hour = alarm_time[0:2]
alarm_second = alarm_time[3:5]
alarm_miute = alarm_time[6:8]
while True:
    time_now = datetime.now()