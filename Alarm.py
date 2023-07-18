from datetime import time


class Alarm:

    def __init__(self):
        self.alarmTime = time(0, 0, 0)

    def set_alarm(self, hour, minute, second):
        if not self.is_set:
            self.is_set = True
            print(f"Alarm set for {seconds} seconds.")
            time.sleep(seconds)
            print("ALARM!")

    def reset_alarm(self):
        self.is_set = False
        print("Alarm reset.")
