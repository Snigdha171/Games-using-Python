############################################################
# Name : NumGame.py
# Date : Nov 13, 2016
# Author : Snigdha Praksh
# Description : This is a game that generates 2 random numbers 
#               and the user has to perform the calculation within 5 seconds
#               
############################################################
#History
# Date          Description
# Nov-13-2016   Initial verion
# Nov-14-2016   Changed the format. Allowing user to play without any prompt if it's a win
# Nov-14-2016   Added random operations and final stats in form of bar chart
#############################################################

import random
import time
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


print('''#######################################################################
Game Description - \n
2 numbers will be displayed on the screen. \nYou need to answer it within 5 seconds
#######################################################################\n''')
Ready = input("Ready? Enter Y/N >> ")
count_of_questions = 0
questions_correct = 0
questions_not_correct = 0
def incrementQN():
    global count_of_questions
    count_of_questions = count_of_questions+1
def incrementQC():
    global questions_correct
    questions_correct =  questions_correct+1
def incrementQNC():
    global questions_not_correct
    questions_not_correct = questions_not_correct+1
try:
    if Ready in ("Y","y"):
        def play():
            num1=random.randint(1,15)
            num2=random.randint(1,15)
            operation=random.choice('+*-')
            print("Evaluate the following : " + str(num1) + operation + str(num2))
            incrementQN()
            startTime = datetime.now().second
            if operation == '+':
                num3=num1 + num2
            elif operation == '-':
                num3=num1 - num2
            else:
                num3=num1 * num2
            ans=int(input("Input sum: "))
            endTime = datetime.now().second
            timeDiff = endTime - startTime
            if(timeDiff < 0):
                timeDiff = 60 - abs(timeDiff)
            if(timeDiff > 5):
                print("You Lost! You took " + str(timeDiff) + " seconds to answer!!")
                incrementQNC()
                time.sleep(1)
                print("Play again?")
                again = input("Y/N >> ")
                if again in ("Y","y"):
                    play()
                else:
                    print("Number of Questions Played - ", count_of_questions)
                    print("Number of Questions Correct - ", questions_correct)
                    print("Number of Questions answered incorrectly - ", questions_not_correct)

            else:
                if(ans == num3):
                    print(" You won! You took " + str(timeDiff) + " seconds to answer!!")
					#print("Play again?")
					#again = input("Y/N >> ")
					#if again == "Y":
                    incrementQC()
                    play()  
                else:
                    print("Incorrect answer. You lost!!\nThe correct answer is " + str(num3))
                    incrementQNC()
                    time.sleep(1)
                    print("Play again?")
                    again = input("Y/N >> ")
                    if again in ("Y","y"):
                        play()
                    else:
                        print("Number of Questions Played - ", count_of_questions)
                        print("Number of Questions Correct - ", questions_correct)
                        print("Number of Questions answered incorrectly - ", questions_not_correct)

        play()				

    else:
        print("Exiting the script")
		
        time.sleep(1)
        print("Number of Questions Played - ", count_of_questions)
        print("Number of Questions Correct - ", questions_correct)
        print("Number of Questions answered incorrectly - ", questions_not_correct)

except ValueError:
    print("You have not provided the result!!So exiting...")
    incrementQNC()
    time.sleep(1)
    print("Number of Questions Played - ", count_of_questions)
    print("Number of Questions Correct - ", questions_correct)
    print("Number of Questions answered incorrectly - ", questions_not_correct)

#Plotting the graph
objects = ('Question played','Correct answer','Incorrect Answer')
y_pos = np.arange(len(objects))
stats = [count_of_questions,questions_correct,questions_not_correct]
plt.bar(y_pos, stats, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Numbers')
plt.title('Game stats')
 
plt.show()