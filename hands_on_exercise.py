"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print (type(pi), pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if(i<50):
    print("i is less than 50")
if (i>50):
    print ("i is greater than 50")
# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit=="strawberry":
    print(" Current collor of strawberry is dark red")
elif picked_fruit=="orange":
    print("Current collor is orange")
elif picked_fruit=="banana":
    print("Current collor of banana is yellow")
# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
value1=int(input("Enter value1:" ))
value2=int(input("Enter value2:" ))

def multiply(value1,value2):
    result = value1*value2
    return result
result=multiply(value1,value2)
print("Multiply of value1 and value2 is=",result)
# TODO: Now call the function a few times to calculate the following answers
print("12 x 96 =",multiply(12,96))
print("48 x 17 =",multiply(48,17))

print("196523 x 87323 =",multiply(196253,87323))


