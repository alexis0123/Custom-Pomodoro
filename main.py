from pomodoro import Timer

timer = Timer(1, 5)

timer.start()
for tick in timer.tick():
    print(f"    {tick}", end="\r")


print("\ndone")