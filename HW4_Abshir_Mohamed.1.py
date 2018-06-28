# Homework 4
# cs120
# Abshir Mohamed
# This is a program that prompts the user for various questions  
# the third part of this program works as follows a software company sells a package that retails for $99. 
# Quantity discounts are given according to the following table. 
# This program will ask for the number of units sold and computes the total cost. 
# 5/24/2018

import random

# Part one
# ****************************************************
test = input("ACT or SAT? ")

score = int(input("What was your score? "))

if test == "ACT":
    if score>=0 and score<=7:
        print ("Needs work")
    elif score >= 10 and score<=20:
        print ("Acceptable")
    elif score>20:
        print ("Above average")
else:
    if score>=200 and score<=400:
        print ("Needs work")
    elif score >= 401 and score<=1000:
        print ("Acceptable")
    elif score>1000:
        print ("Above average")
    

# Part two
# ****************************************************

for i in range(11):
    num = random.randint(25,100)  
    if num >= 0 and num<=59:
        print ("F")
    elif num >= 60 and num<=69:
        print ("D")
    elif num >= 70 and num<=79:
        print ("C")
    elif num >= 80 and num<=89:
        print ("B")
    elif num>90:
        print ("A")



# Part three
# ****************************************************

user = int(input("Pick 1=Rock,2=Paper,or3=Scissors "))
comp = random.randint(1,3)


print("Rock Paper Scissors Shoot!")

if user==1 and comp==3:
    print("You win!Rock beats Scissors")
elif user == 2 and comp == 1:
    print("You win!Paper beats Rock")
elif user == 3 and comp == 2:
    print("You win!Scissors beats Paper") 
elif user == 3 and comp == 1:
    print("You lose!Rock beats Scissors")
elif user == 1 and comp == 2:
    print("You lose!Paper beats Rock")
elif user == 2 and comp == 3:
    print("You lose!Scissors beats Paper") 
else:
    print("Tie Game!") 

  
