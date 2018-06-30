# Homework 5
# cs120
# Abshir Mohamed
# This is a program that runs a bunch of implements 6 different python methods for their respected uses 
# 6/1/2018

import math,random

# Part one
# ****************************************************

def drawBox():
    print ("+-----+")
    print ("|     |")
    print ("|     |")
    print ("+-----+")

def drawLadder():
    for i in range(1,6):
        print ("|     |")
        drawBox()

drawLadder()


# Part two
# ****************************************************

def plusRoot(a,b,c):
    negB = int(b*-1)
    square = float(math.sqrt(math.pow(b,2)-(4*a*c))) 
    top = negB+square
    bottom = 2*a
    return float(top/bottom)

def minusRoot(a,b,c):
    negB = int(b*-1)
    square = float(math.sqrt(math.pow(b,2)-(4*a*c))) 
    top = negB-square
    bottom = 2*a
    print (float(top/bottom))


print (plusRoot(4,-24,35))

minusRoot(4,-24,35)
    
# Part two
# ****************************************************    

def Collatz(num):
    if num%2==0:
        return num//2
    else:
        return  (3 * num + 1)

def Collatz2(num):
    print(num)
    while num!=1:
        num = Collatz(num)
        print(num)

Collatz2(5)
