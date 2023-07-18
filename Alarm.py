from datetime import time


class Alarm:

    def __init__(self):
        self.activated = False
        self.alarmTime = time(0, 0, 0)

    def set_alarm(self, hour, minute, second):
        self.activated = True
        self.alarmTime = time(hour, minute, second)
        print("Alarm set at " + str(self.alarmTime))

    def clear(self):
        self.alarmTime = time(0, 0, 0)
        self.activated = False


if __name__ == '__main__':
    alarm = Alarm()
    alarm.set_alarm(12, 0, 0)
    print("{"+"hour: {}, minute: {}, second: {}".format(alarm.alarmTime.hour, alarm.alarmTime.minute, alarm.alarmTime.second)+"}")
