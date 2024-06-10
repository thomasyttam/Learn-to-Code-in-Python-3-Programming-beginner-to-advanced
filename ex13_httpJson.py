import requests
import json
import random

GoOn = True
score = 0

while GoOn:
    result = requests.get("https://opentdb.com/api.php?amount=1&category=17&difficulty=easy&type=multiple")
    print(result)
    if result.status_code == 200: #check if the request is successful
        data = json.loads(result.text)
        question = data['results'][0]['question']
        print(question)
        answers = data['results'][0]['incorrect_answers']
        correctAnswer = data['results'][0]['correct_answer']
        answers.append(correctAnswer)
        random.shuffle(answers)
        for i in range(len(answers)):
            print(i+1, answers[i])
        userAnswer = int(input("Please enter the number of the correct answer: "))
        if answers[userAnswer-1] == correctAnswer:
            print("Congratulations! You are correct.")
            score += 1
        else:
            print("Sorry, the correct answer is", correctAnswer)
        print("Your current score is", score)
        answer = input("Do you want to play again? (yes/no): ")
        if answer.lower() == "quit":
            print("Thank you for playing the game.")
            GoOn = False