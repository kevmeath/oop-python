class Clock(object):
    def __init__(self, hours: int, minutes: int, seconds: int):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._alarm_time = ""
        self._alarm_set = False

    def check_time(self, time: str) -> bool:
        try:
            time_list = time.split(':')
            int(time_list[0])
            int(time_list[1])
            int(time_list[2])
        except:
            return False
        else:
            if (0 <= int(time_list[0]) <= 23) and (0 <= int(time_list[1]) <= 59) and (0 <= int(time_list[2]) <= 59) and (len(time_list) == 3):
                return True
            else:
                return False

    def change_time(self, time: str) -> None:
        if self.check_time(time):
            time_list = time.split(':')
            self._hours = int(time_list[0])
            self._minutes = int(time_list[1])
            self._seconds = int(time_list[2])

    def __str__(self):
        print(self._hours,':',self._minutes,':',self._seconds)

    def add_time(self, time: str) -> None:
        pass

    def set_alarm(self, time: str) -> None:
        self._alarm_time = time
        self._alarm_set = True

    def ring_alarm(self, time: str) -> None:
        self._alarm_set = False
        print("!!! ",self._alarm_time," !!!")
