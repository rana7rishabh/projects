import pyttsx3
questions = [
["Who is Shah Rukh Khan?", "Plumber", "Astronaut", "Actor", "WWE Wrestler", "c"],
["What is the capital of France?", "Rome", "London", "Berlin", "Paris", "d"],
["Which planet is known as the Red Planet?", "Mars", "Earth", "Venus", "Jupiter", "a"],
["What is the largest mammal?", "Blue Whale", "Shark", "Elephant", "Giraffe", "a"],
["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Homer", "Charles Dickens", "a"],
["What is the square root of 64?", "12", "6", "10", "8", "d"],
["Which country is known as the Land of the Rising Sun?", "China", "South Korea", "Japan", "India", "c"],
["Who painted the Mona Lisa?", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", "Vincent van Gogh", "b"],
["What is the fastest land animal?", "Lion", "Cheetah", "Horse", "Elephant", "b"],
["Which ocean is the largest?", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "Atlantic Ocean", "c"],
["What is the smallest country in the world?", "Vatican City", "San Marino", "Liechtenstein", "Monaco", "a"]
]

for i in questions:
    engine = pyttsx3.init()
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

    ans=input("Choose the correct answer: ")
    if ans==i[5]:
        engine.say("satt crooooooore")
        engine.runAndWait()
        print("saaaaaaaatttttt crooooooore")
    else:
        engine.say(f"ye galat jawaab hai. sahi jawaab {i[5]} haaayyy")
        engine.runAndWait()
        print(f"ye galat jawaab hai. sahi jawaab {i[5]} haaayyy")
        break
