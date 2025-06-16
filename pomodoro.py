from datetime import date, datetime, timedelta
from time import sleep

class Timer:
    def __init__(self, duration, break_time):
        duration = timedelta(seconds = duration * 60)
        break_time = timedelta(seconds = break_time * 60)

        self.started = datetime.now()
        self.duration = int(duration.total_seconds())
        self.break_time = int(break_time.total_seconds())
        self.running = False

    def start(self):
        self.running = True

    def tick(self):
        while self.duration > 0:
            mins, secs = divmod(self.duration, 60)

            if self.running:
                yield(f"{mins:02d}:{secs:02d}")
                sleep(1)
                self.duration -= 1

            else:
                yield(f"{mins:02d}:{secs:02d}")
                sleep(1)
                yield("_    ")
                sleep(1)

    def pause(self):
        self.running = False