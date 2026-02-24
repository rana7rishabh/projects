import time
import pyttsx3
engine = pyttsx3.init()
current_time=(time.strftime("%H:%M:%S")) #In (Str)type & time in 24 hours format
hour=int(time.strftime("%H"))
min=int(time.strftime("%M"))
sec=int(time.strftime("%S"))
print("Current Time:", current_time)

if hour < 0 and hour < 12:
    print(f"Good Morning the time is {hour}:{min} AM")
    engine.say(f"Good Morning the time is {hour}, {min} AM")
    engine.runAndWait()
elif hour >=12 and hour<17:
    print(f"Good Afternoon the time is {hour}:{min} PM")
    engine.say(f"Good Afternoon the time is {hour}, {min} PM")
    engine.runAndWait()
elif hour >=17 and hour <20:
    print(f"Good Evening the time is {hour}:{min} PM")
    engine.say(f"Good Evening the time is {hour} {min} PM")
    engine.runAndWait()
    
else:
    print(f"Good Night the time is {hour}:{min} PM")
    engine.say(f"Good Night the time is {hour}, {min} PM")
    engine.runAndWait()
