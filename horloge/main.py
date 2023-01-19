
import datetime
import time


def afficher_heure():
    heure_machine = datetime.datetime.now()
    print(heure_machine.strftime("%H:%M:%S"))


def regler_heure(heure):
    global current_time
    current_time = heure


def regler_alarme(alarme):
    global alarm_time
    alarm_time = alarme


current_time = datetime.datetime.now()
alarm_time = current_time + datetime.timedelta(seconds=30)

while True:
    afficher_heure()
    if current_time == alarm_time:
        print("Alarme!")
    time.sleep(1)
    current_time = datetime.datetime.now()

