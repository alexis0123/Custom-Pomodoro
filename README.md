Logs pomodoros and daily streaks to JSON. I use it to track how often I actually show up.


## 💡 Features
- Start a 25-minute Pomodoro session from the terminal
- Logs session time and task name
- Tracks how many pomodoros per task
- Tracks your daily streak
- Lets you reflect on finished tasks
- Stores everything in a local JSON file
- Plays system alarm on session end (Linux)


## 📦 Requirements

- Python 3.10+
- Linux with `paplay` (PulseAudio) for alarms


## 🛠️ Setup

```bash
git clone https://github.com/devout-a/Custom-Pomodoro.git
cd Custom-Pomodoro
python3 main.py "Name of your task"

```

## Example use

python3 main.py "Study Kotlin"


## Example output

- Daily streak : 5
- "Study Kotlin" : 3 pomos
- Start pomodoro [ENTER]
- Finish Task [F]



