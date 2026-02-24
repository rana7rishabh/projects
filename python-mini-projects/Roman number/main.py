num=input("Enter a roman numerals you want to convert: ")
def roman(numeral):
    final_answer=0
    for i in num:
        if i == "M":
            final_answer += 1000
        elif i == "D":
            final_answer += 500
        elif i == "C":
            final_answer += 100 
        elif i == "L":
            final_answer += 50
        elif i == "X":
            final_answer += 10
        elif i == "V":
            final_answer += 5
        elif i=="I":
            final_answer+= 1
        else:
            print("Invalid Input")

    print("The Roman numerals you entered translate to: ", final_answer)
                       
  
roman(num)

