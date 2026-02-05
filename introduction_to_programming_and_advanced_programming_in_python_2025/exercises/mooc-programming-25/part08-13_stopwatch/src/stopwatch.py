# # 1 - FIRST SOLUTION
# class Stopwatch:
#     def __init__(self):
#         self.seconds = 0
#         self.minutes = 0

#     def __str__(self):
#         return f"{self.minutes:02d}:{self.seconds:02d}"

#     def tick(self):
#         self.seconds += 1
#         if self.seconds == 60:
#             self.seconds = 0
#             self.minutes += 1
#             if self.minutes == 60:
#                 self.minutes = 0

# 2 - SECOND SOLUTION
class Stopwatch():
    def __init__(self):
        self.total_seconds = 0

    def __str__(self):
        seconds = self.total_seconds % 60
        minutes = self.total_seconds // 60 % 60
        return f"{minutes:02d}:{seconds:02d}"

    def tick(self):
        self.total_seconds += 1

if __name__ == "__main__":
    from time import sleep # module time has function sleep() that can wait a preset amount of seconds
    watch = Stopwatch()
    for i in range(11): # test also range(3602) to see that it works
        print(watch)
        watch.tick()
        sleep(1) # makes each second timestamp appear after (really) 1 second
