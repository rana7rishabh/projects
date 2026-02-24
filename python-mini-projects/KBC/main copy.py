import pyttsx3
import speech_recognition as sr
r = sr.Recognizer()
engine = pyttsx3.init()

questions = [
["Who is Shah Rukh Khan?", "Plumber", "Astronaut", "Actor", "WWE Wrestler", "c", 3],
["What is the capital of France?", "Rome", "London", "Berlin", "Paris", "d", 4],
["Which planet is known as the Red Planet?", "Mars", "Earth", "Venus", "Jupiter", "a", 1],
["What is the largest mammal?", "Blue Whale", "Shark", "Elephant", "Giraffe", "a", 1],
["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Homer", "Charles Dickens", "a", 1],
["What is the square root of 64?", "12", "6", "10", "8", "d", 4],
["Which country is known as the Land of the Rising Sun?", "China", "South Korea", "Japan", "India", "c", 3],
["Who painted the Mona Lisa?", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", "Vincent van Gogh", "b", 2],
["What is the fastest land animal?", "Lion", "Cheetah", "Horse", "Elephant", "b", 2],
["Which ocean is the largest?", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "Atlantic Ocean", "c", 3],
["What is the smallest country in the world?", "Vatican City", "San Marino", "Liechtenstein", "Monaco", "a", 1]
]

for i in questions:
    print(i[0])
    engine.say(i[0])
    engine.runAndWait()
    print("Options:-")
    engine.say("Options")
    engine.runAndWait()
    print('a.',i[1])
    engine.say(f"a, {i[1]}")
    engine.runAndWait()
    print('b.',i[2])
    engine.say(f"b, {i[2]}")
    engine.runAndWait()
    print('c.',i[3])
    engine.say(f"c, {i[3]}")
    engine.runAndWait()
    print('d.',i[4])
    engine.say(f"d, {i[4]}")
    engine.runAndWait()

    print("Choose the correct answer: ")
    with sr.Microphone() as source:

        print("Speak now...")
        audio_data = r.listen(source, timeout=5) # Listen for 5 seconds
        print("Listening to the answer")
        try:
            ans = r.recognize_google(audio_data)
            print(ans)
            ans = ans.lower().strip()
            if ans in [i[5], i[i[6]].lower(), f"{i[5]} {i[i[6]].lower()}", f"{i[i[6]].lower()}"]:
                engine.say("satt crooooooore")
                engine.runAndWait()
                print("saaaaaaaatttttt crooooooore")
            else:
                corr_ans=(int(i[6]))
                engine.say(f"ye galat jawaab hai. sahi jawaab {i[corr_ans]} haaayyy")
                engine.runAndWait()
                print(f"ye galat jawaab hai. sahi jawaab {i[5]} haaayyy")
                break
        except sr.UnknownValueError:
            print("Could not understand your audio")

