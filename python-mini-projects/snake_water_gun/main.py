import random
while True:
    list=[0, "Stone", "Paper", 'Scissor']
    com_choice=random.randrange(1,len(list))
    player_choice=int(input('''
                            1. Stone
                            2. Paper
                            3. Scissor
                            Enter a your choice: '''))
    if player_choice==1 and com_choice==1:
        print(f"computer choice: {list[com_choice]}")
        print("Draw")
    elif player_choice==2 and com_choice==2:
        print(f"computer choice: {list[com_choice]}")
        print("Draw")
    elif player_choice==3 and com_choice==3:
        print(f"computer choice: {list[com_choice]}")
        print("Draw")
    elif player_choice==1 and com_choice==2:
        print(f"computer choice: {list[com_choice]}")
        print("computer won")
    elif player_choice==2 and com_choice==1:
        print(f"computer choice: {list[com_choice]}")
        print("You won")
    elif player_choice==2 and com_choice==3:
        print(f"computer choice: {list[com_choice]}")
        print("computer won")
    elif player_choice==3 and com_choice==2:
        print(f"computer choice: {list[com_choice]}")
        print("You Won")
    elif player_choice==3 and com_choice==1:
        print(f"computer choice: {list[com_choice]}")
        print("com won")
    elif player_choice==1 and com_choice==3:
        print(f"computer choice: {list[com_choice]}")
        print("you won")
    else:
        print("invalid input")

