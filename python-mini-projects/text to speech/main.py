import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:

    print("Speak now...")
    audio_data = r.listen(source, 5) # Listen for 5 seconds
    print("Recognizing...")
    text = r.recognize_google(audio_data)
    print(text)