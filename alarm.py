from datetime import datetime
from playsound import playsound
from colorama import Fore
alarm_time = input(Fore.BLUE + "Enter a time for alarm with this format (HH:MM) >> ")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_title = input(Fore.BLUE + "set your alarm title >> ")
while True:
    print(Fore.YELLOW +  "proccesing for alarm")
    time_now = datetime.now()
    c_hour = time_now.strftime("%H")
    c_minute = time_now.strftime("%M")

    if alarm_hour == c_hour:
        if alarm_minute == c_minute:
                print(Fore.LIGHTMAGENTA_EX + "Alarm!!!!!!!!!!!")
                print(Fore.GREEN + alarm_title)
                playsound("alarm.mp3")
                break
