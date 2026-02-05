# Write your solution here:
class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        if self.hour_ok(hours):
            self.hours = hours
        if self.min_sec_ok(minutes):
            self.minutes = minutes
        if self.min_sec_ok(seconds):
            self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def hour_ok(self, hour: int):
        return True if 0 <= hour <= 23 else False

    def min_sec_ok(self, min_sec: int):
        return True if 0 <= min_sec <= 59 else False

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours +=1
                if self.hours == 24:
                    self.hours = 0

    def set(self, hours: int, minutes: int):
        if self.hour_ok(hours):
            self.hours = hours
        if self.min_sec_ok(minutes):
            self.minutes = minutes
        self.seconds = 0

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

# 23:59:55
# 23:59:56
# 23:59:57
# 23:59:58
# 23:59:59
# 00:00:00
# 00:00:01
# 12:05:00
# 12:05:01
# 12:05:02
