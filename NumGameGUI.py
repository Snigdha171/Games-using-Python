############################################################
# Name : NumGameGUI.py
# Date : Nov 16, 2016
# Author : Snigdha Praksh
# Description : This is a game that present GUI which displays 2 random numbers 
#               and the user has to perform the calculation within 5 seconds
#               
############################################################
#History
# Date          Description
# Nov-16-2016   Initial verion
# Nov-18-2016   Customized the bar plot
# Nov-18-2016   Handled blank value in input text box
#############################################################

#Importing required modules
import tkinter as tk
import random
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

master = tk.Tk()

#Set the title of the frame
master.title('Number Game')

#Set the frame size
master.geometry("400x200")

#Defining Global variables
userAnswer=None
sysAnswer=None
startTime=None
endTime=None
timeDiff=None
count_of_questions = 0
questions_correct_wt = 0
questions_correct_bt = 0
questions_not_correct = 0


#Defining functions to increment the value of result variables
def incrementQ():
    global count_of_questions
    count_of_questions += 1
def incrementQCWT():
    global questions_correct_wt
    questions_correct_wt += 1
def incrementQCBT():
    global questions_correct_bt
    questions_correct_bt += 1
def incrementQNC():
    global questions_not_correct
    questions_not_correct += 1
	

#Block for getting subsequent questions
def getQuestion():
    
    global sysAnswer
    global userAnswer
    global startTime
    entry.focus_set()
    entry.delete(0, tk.END)
    num1=random.randint(1,15)
    num2=random.randint(1,15)
    operation=random.choice('+*-')
    
    if operation == '+':
        sysAnswer=num1 + num2
    elif operation == '-':
        sysAnswer=num1 - num2
    else:
        sysAnswer=num1 * num2

    qt = str(num1) + operation + str(num2)
    text="Evaluate the expression within 5 seconds\n" + str(qt)
    question.config(text=text)
    question.pack()
    startTime = datetime.now().second
    incrementQ()


#Block for evaluating the answer and collecting the data
def evaluate(event):
    global userAnswer
    global sysAnswer
    global startTime
    endTime = datetime.now().second
    timeDiff = endTime - startTime
    if(timeDiff < 0):
        timeDiff = 60 - abs(timeDiff)
    userAnswer = entry.get()
    if userAnswer == "":
        warn.configure(text = "Answer field cannot be left blank. Please enter a value!!")
    else:
        warn.configure(text = "")
        
    if int(userAnswer) == int(sysAnswer):
        #If answer is correct, check if time difference is less than 5
        if(timeDiff < 5):
            res.configure(text = "\nCorrectly answered! You have answered within time")
            incrementQCWT()
        else:
            res.configure(text = "\nCorrectly answered but you have taken more than 5 seconds!!")
            incrementQCBT()
    else:
        res.configure(text = "\nWrong! The correct value is : " + str(sysAnswer))
        incrementQNC()
    getQuestion()

def endGame():
    print("No. of questions attempted - " + str(int(count_of_questions)-1) + "\nNo. of questions correctly answered within time - " + str(questions_correct_wt))
    print("No. of questions correctly answered beyond time - " + str(questions_correct_bt) + "\nNo. of questioned not answered correctly - " + str(questions_not_correct))
    master.destroy()
	
#First run of the program
num1=random.randint(1,15)
num2=random.randint(1,15)
operation=random.choice('+*-')
    
if operation == '+':
    sysAnswer=num1 + num2
elif operation == '-':
    sysAnswer=num1 - num2
else:
    sysAnswer=num1 * num2

qt = str(num1) + operation + str(num2)
text="Evaluate the expression within 5 seconds\n" + str(qt)
question = tk.Label(master, text=text)
question.pack()
incrementQ()
startTime = datetime.now().second
tk.Label(master, text="Answer:").pack()
entry = tk.Entry(master)
entry.bind("<Return>", evaluate)
entry.pack()

warn = tk.Label(master)
warn.pack()

res = tk.Label(master)
res.pack()

#Exiting on click of a button
exitButton = tk.Button(master, text="End the game", command=endGame, fg="#ff0000")
exitButton.pack(side="top")

#Starting point of GUI
master.mainloop()

total_questions = count_of_questions - 1

#Plotting the bar graph

if str(total_questions) != "0":
    plt.figure(0)
    ax1 = plt.subplot2grid((1,1), (0,0))
    objects = ('Total Number of Questions','Correctly Answered within Time','Correctly Answered beyond time', 'Incorrectly answered')
    y_pos = np.arange(len(objects))
    stats = [total_questions,questions_correct_wt,questions_correct_bt,questions_not_correct]
    #plt.bar(y_pos, stats, align='center', alpha=0.5, facecolor='#9999ff')
    ax1.bar(y_pos, stats, align='center', alpha=0.5, facecolor='#9999ff')
    plt.xticks(y_pos, objects)
    plt.ylabel('Numbers')
    plt.title('Your Result!') 
	 
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90)

#Plotting the pie chart

if str(total_questions) != "0":
    plt.figure(1)
    labels = 'Correctly Answered within Time','Correctly Answered beyond time','Incorrectly answered'
    sizes = [questions_correct_wt,questions_correct_bt,questions_not_correct]
    colors = ['green', 'orange','red']
    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')

#Show both the graphs
plt.show()
