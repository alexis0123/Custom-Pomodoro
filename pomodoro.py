from datetime import date, datetime, timedelta
from time import sleep

class Timer:
    def __init__(self, duration):
        self.started = datetime.now()
        self.duration = timedelta(seconds = duration * 60)

        self.running = False
        self.ticking = False

    def start(self):
        self.running = True
        self.ticking = True

    def tick(self):
        while self.duration > timedelta(seconds=0):
            mins, secs = divmod(int(self.duration.seconds), 60)

            yield(f"{mins:02d}:{secs:02d}")
            sleep(1)

            if not self.running:
                continue
            
            self.duration -= timedelta(seconds=1)

        yield "00:00"
        self.ticking = False
        self.running = False

    def pause(self):
        self.running = False