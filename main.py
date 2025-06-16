from pomodoro import Timer
import sys

def timer(mins):
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
            print(f"   {tick}", end="\r", flush=True)
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
                sys.exit()

        except StopIteration:
            break

    print("   00:00 [DONE]")

def main():
    timer(25)

if __name__ == "__main__":
    main()