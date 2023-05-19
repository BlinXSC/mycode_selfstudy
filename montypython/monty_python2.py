#!/usr/bin/env python3
"""TLG Learning | AAlegre
   Conditionals - Life of Brian guessing game using a while True loop."""

# Initializes round counter and answer
round = 0
answer = ""

while round < 3 and (answer != "brian" and answer!= "shrubbery"):
    round +=1 # Adds to the round counter

    # Prompts the user to finish the movie title
    answer = input('Finish the movie title: "Monty Python\'s The Life of _____" --> ')

    # Turns the string into all lower case letters
    answer = answer.lower()    

    # Program responds accoring the user's response.
    if answer == 'brian':
        print("Correct")
    elif answer == 'shrubbery':
        print("You gave the super secret answer!")
    elif round == 3:
        print('Sorry, the answer was Brian.')
    else:
        print("Sorry, please guess again.")

