# Guess the number game:

import random

number=random.randint(1,50)

guesses=0

while guesses<5:
	print ("Hey user, please guess the number between 1-50, you have {} chance".format(5-guesses))
	user_input=int(input("Enter your guess"))
	guesses+=1
	
	if user_input < number:
		print ("your guess is too low")
	elif user_input > number:
		print ("your guess is little bit high")
	elif user_input==number:
		print ("Hurray, you guess the right number")
		break
if user_input==number:
	print ("Your guess it in {} time".format(guesses))

if user_input!=number:
	print ("The secret number is {}".format(number))

print("Thanks for playing the game , hope you will come back again !!!!!!")
