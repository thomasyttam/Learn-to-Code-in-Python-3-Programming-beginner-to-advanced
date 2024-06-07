import random

colorList=["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", 
           "white", "pink", "purple", "brown", "gray", "silver", "gold"]

print("Please guess the color from the following list")

for color in colorList:
    print(color, end=" ")
print()
color = colorList[random.randint(0,len(colorList)-1)]

while True:
    guessColor = input("Please enter your guess: ")
    if guessColor.lower() == color:
        print("Congratulations! You guessed the correct color. The color is", color)
        answer = input("Do you want to play again? (yes/no): ")
        if answer.lower() == "no":
            print("Thank you for playing the game.")
            break
        else:
            color = random.choice(colorList)
    else:
        print("The color you entered is not in the list. Please try again.")