############################################################
# Name : AddNumGame.py
# Date : Nov 13, 2016
# Author : Snigdha Praksh
# Description : This is a game that generates 2 random numbers 
#               and the user has to answer it within 3 seconds
#               
############################################################
#History
# Date          Description
# Nov-13-2016   Initial verion
#############################################################

import random
from datetime import datetime

print('''#######################################################################
Game Description - \n
2 numbers will be displayed on the screen. \nYou need to answer it within 3 seconds
#######################################################################\n''')
Ready = input("Ready? Enter Y/N >> ")
if Ready == "Y":
    def play():
        num1=random.randint(1,25)
        num2=random.randint(1,25)
        print("The numbers are : " + str(num1) + "+" + str(num2))
        startTime = datetime.now().second
        num3=num1 + num2
        ans=int(input("Input sum: "))
        endTime = datetime.now().second
        timeDiff = endTime - startTime
        if(timeDiff < 0):
            timeDiff = 60 - abs(timeDiff)
        if(timeDiff > 3):
            print("You Lost! You took " + str(timeDiff) + " seconds to answer!!")

        else:
            if(ans == num3):
                print(" You won! You took " + str(timeDiff) + " seconds to answer!!")
                print("Play again?")
                again = input("Y/N >> ")
                if again == "Y":
                    play()  
            else:
                print("Incorrect answer. You lost!!")

    play()				

else:
    print("Exiting the script")
   