import time as t
import matplotlib.pyplot as plt
import random

wordList = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon', 'xigua', 'yam', 'zucchini']

timeList = []
wordtyped =[]
mistakes = 0

word = wordList[random.randint(0, len(wordList)-1)] #choose a random word from the list
    
print("Please type " + word + " five times as fast as you can.")
input("Press Enter to start...")
for i in range(5): #repeat the process five times
    start = t.time()
    userInput = input()
    end = t.time()
    if userInput != word:
        mistakes += 1
    timeList.append(end-start)
    wordtyped.append(i+1)

print("You made ", mistakes, "mistakes.")
x = wordtyped
y = timeList

#plot the graph
plt.plot(x, y)
plt.xticks(x,x)
plt.xlabel('Attempts')
plt.ylabel('Time')
plt.title('Typing Speed')
plt.show()