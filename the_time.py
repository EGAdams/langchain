import datetime

class Time:
    def __init__(self):
        self.current_time = datetime.datetime.now().strftime("%H:%M:%S")

    def get_current_time(self):
        return self.current_time

time = Time()
print(time.get_current_time())