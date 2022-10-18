import time
from data import *
import schedule

DAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#test
physics = EventCell("Physics")
maths = EventCell("maths")
empty = Empty()

temp = [empty]*96

#14:00-15:00



d = Day()
d.cells[Day.getIndex("14:00")] = physics
d.cells[Day.getIndex("14:15")] = physics
d.cells[Day.getIndex("14:30")] = physics
d.cells[Day.getIndex("14:45")] = physics

d.cells[Day.getIndex("15:00")] = maths
print(d.getNotify())

def newSchedule():
    week = Week()
    




def test():
    print("test")   

def saveData():
    pass


def scheduleRun():
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except:

            break

def main():
    while True:
        print("Schedule Master")
        print("1. Start Schedule\n2. Modify Schedule\n3. New Schedule\nEnter anything else to leave this application.")
        userinput = input()
        if userinput == "1":
            scheduleRun()
        elif userinput == "2":
            pass
        elif userinput == "3":
            pass
        else:
            saveData()
            break