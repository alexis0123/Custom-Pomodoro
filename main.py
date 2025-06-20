from datetime import datetime
import os
from pomodoro import Timer
import sys
from storage import data
import sys

def time():
    return datetime.now().strftime("%I:%M %p")

def alarm():
    os.system("paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga")

def timer(mins) -> bool:
    timer = Timer(mins)
    timer.start()
    tick_gen = timer.tick()

    print("   Ctrl+c to PAUSE\n")
    print(f"   Start   : {timer.started.strftime('%I:%M %p')}")
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
        print("Finished tasks:")
        for line in data.get_tasks():
            task = line["task"]
            if len(task) > 20:
                task = line["task"][:20] + "..."
            print(f"  {task} : {line['pomos']} pomos")
        sys.exit()
        
    cur_task = data.add_task(sys.argv[1])
    time_start = time()

    while True:
        os.system("clear")

        task = data.get_tasks()[-1]
        cur_pomos = task["pomos"]

        task = cur_task
        if len(cur_task) > 25:
            task = cur_task[:25] + "..."
        print(f"\"{task}\" : {cur_pomos} pomos")

        print("Start pomodoro [ENTER]")
        if cur_pomos:
            print("Finish Task [F]")
            
        try:
            prompt = input().strip().lower()
        except KeyboardInterrupt:
            os.system("clear")
            input("[F] To finish task")

        if prompt == "f" and cur_pomos:
            reflection = input("Reflection: \n")
            data.add_reflection(cur_task, reflection)
            data.save()
            break

        os.system("clear")
        if timer(25):
            print(cur_task)
            data.add_pomo(cur_task, time_start, time())
            alarm()
        else:
            continue
        
        os.system("clear")
        print("BREAK TIME")
        timer(5)
        alarm()

if __name__ == "__main__":
    main()