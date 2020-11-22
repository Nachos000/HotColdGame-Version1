#import the modul for random numbers and letters
import random

#introduction
print('Welcome to my Hot/Cold Game')
print('I will create a number between 0 and 100 and you have to guess the number')

#create a random number between 0 and 100
x=random.randint(0,100)

#while true loop
while True:
    a=input('Guess a number between 0 and 100:    ')
    a=int(a) #makes the input an integer
    if a==x: #you guessed the right number
        print('Congratulations! you guessed the right number')
        break
    elif a>x: #you guessed too high
        print('the number you guessed was too HIGH')
        print('the number is somewhere under the number you guessed:    ')
    elif a<x: #you guessed too low
        print('the number you guessed was too LOW')
        print('the number is somewhere over the number you guessed:    ')
    else: #you write a letter doesnt work :(
        print('please write a number')