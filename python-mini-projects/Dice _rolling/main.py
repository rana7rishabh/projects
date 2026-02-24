import random
print ("\u25CF \u250C \u2500 \u2510 \u2514 \u2518")

# ● ┌ ─ ┐ └ ┘
"┌─────────┐"
"|         |"
"|         |"
"|         |"
"└─────────┘"
dice_dic={
    1:("┌─────────┐",
       "|         |",
       "|    ●    |",
       "|         |",
       "└─────────┘"),
    2:("┌─────────┐",
       "|  ●      |",
       "|         |",
       "|      ●  |",
       "└─────────┘"),
    3:("┌─────────┐",
       "|  ●      |",
       "|    ●    |",
       "|      ●  |",
       "└─────────┘"),
    4:("┌─────────┐",
       "|  ●   ●  |",
       "|         |",
       "|  ●   ●  |",
       "└─────────┘"),
    5:("┌─────────┐",
       "|  ●   ●  |",
       "|    ●    |",
       "|  ●   ●  |",
       "└─────────┘"),
    6:("┌─────────┐",
       "|  ●   ●  |",
       "|  ●   ●  |",
       "|  ●   ●  |",
       "└─────────┘"),
}

dice=[]
total=0
num=int(input("How many dice you want to roll: "))

for i in range(num):
    dice.append(random.randint(1,6))

for i in range(num):
    for line in dice_dic.get(dice[i]):
        print(line)
for i in dice:
    total+=i
print(f"Total: {total}")