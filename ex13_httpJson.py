import requests
import json
import random

GoOn = True
url = "https://opentdb.com/api.php?amount=1&category=17&difficulty=easy&type=multiple"
score = 0

while GoOn:
    result = requests.get(url)
    
    if result.status_code == 200: # check if the request is successful
        data = json.loads(result.text)
        question = data['results'][0]['question']
        
        # get the answers from json data
        answers = data['results'][0]['incorrect_answers']
        correctAnswer = data['results'][0]['correct_answer']
        answers.append(correctAnswer)
        random.shuffle(answers)
        print(question)

        for i in range(len(answers)):
            print(i+1, answers[i])
        
        invalidAnswer = True

        while invalidAnswer: # check if the answer is valid
            try:
                userAnswer = int(input("Please enter the number of the correct answer: ")) #check if the answer is integer
                
                if userAnswer < 1 or userAnswer > len(answers): #check if the answer is within the range
                    print("Please enter an integer from 1 to", len(answers))
                else:
                    if answers[userAnswer-1] == correctAnswer:
                        print("Congratulations! You are correct.")
                        score += 1
                        invalidAnswer = False
                    else:
                        print("Sorry, the correct answer is", correctAnswer)
                        invalidAnswer = False
            except:
                print("Please enter a number from 1 to", len(answers), "only"   )

        print("Your current score is", score)
        answer = input("Do you want to play again? (yes/no): ")
        
        if answer.lower() == "no":
            print("Thank you for playing the game.")
            GoOn = False
        elif answer.lower() == "yes":
            GoOn = True
        else:
            print("Invalid input. The game will be terminated.")
            GoOn = False
    else:
        print("Sorry, the request is not successful. Please try again later.")
        GoOn = False