from datetime import datetime
from pomodoro import Timer
import sys
from storage import data
import sys

def time():
    return datetime.now().strftime("%I:%M %p")

def timer(mins) -> bool:
    timer = Timer(mins)
    timer.start()
    tick_gen = timer.tick()

    print("   Ctrl+c to PAUSE\n")
    print(f"   Start:    {timer.started.strftime('%I:%M %p')}")
    print(f"   Est. end: {(timer.started + timer.duration).strftime('%I:%M %p')}")
    print(f"   {'-'*18}")
    while timer.ticking:
        try:
            tick = next(tick_gen)
            print(f"   {tick}     ", end="\r", flush=True)
        except KeyboardInterrupt:
            timer.pause()
            print(f"\r   {tick} [PAUSED] Enter to resume or Ctrl+c to quit", end="\r", flush=True)
            try:
                input()
                print("\033[A\033[K", end="")
                timer.start()
                tick_gen = timer.tick()
            except KeyboardInterrupt:
                print("\r   [ABANDONED]", "  "*20)
                return False

        except StopIteration:
            break

    print("   00:00 [DONE]")
    return True

def main():
    if len(sys.argv) < 2:
        print("Missing [TASK] arg")
        sys.exit()
        
    task = data.add_task(sys.argv[1])
    time_start = time()

    while True:
        if timer(25):
            data.add_pomo(task, time_start, time())
            data.save()
        else:
            break

if __name__ == "__main__":
    main()