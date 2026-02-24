import pyttsx3
def speak():
    a= input("Enter what you want to speak: ")
    if a=="exit" or a=="quit":
        print("Exiting the program.")
    else:
        while True:
            print("Speaking...")
            engine = pyttsx3.init()
            engine.say(a)
            engine.runAndWait()
            break
        speak()
           
speak()