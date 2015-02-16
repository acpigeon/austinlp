# -*- coding: utf-8 -*-
#The computer guesses the user's number
"""
    >>> python computer_guess_number.py
    
    From easy to hard, some assignments might be:
    write print statements to understand the flow of the program
    change the names of the functions and variables to more meaningful names
    add a shebang
    write a doctest
    change the game to guess something else
    add score keeping
    write unittests -- some interesting challenges involved that the learner could discover
    refactor the code -- there are definitely some improvements needed
    combine the two programs in alternating turns between the user guessing the computer's number and the
        computer guessing the user's number
    change the program so that it could be used as the logic in a web page
"""
import random

def main ():

    yes_tuple = ("YES", "yes","Yes","Y","y")
    print ("Welcome")
    print ("This time I want to guess a number.")
    print("Pick a number from 1 to 10 but don't tell me.")
    guesses = range(1,11)
    game_on = True
    while game_on:
        try_again = True
        index =  random.randint(0, len(guesses)-1)
        number = guesses.pop( index ) 
    
        if raw_input ("Are you ready? y or n: ") in yes_tuple:
            #to do my_number = int(raw_input("Enter your number. I promise not to look.") )
            if raw_input("I guess {}. Is that what you picked? y or n: ".format(number) ) in yes_tuple:
                if raw_input("I win. Play again? y or n: ") in yes_tuple:
                    continue
                else:
                    game_on=False
                    try_again = False
                    break
            #else
        else: #Are you ready?
            if raw_input("Do you want to play or not? y or n:  ") in yes_tuple:
                continue
            else:
                try_again = False
                break
    
        while try_again:
            if raw_input("Can I guess again? y or n: ") in  yes_tuple:
                if len(guesses)==0:
                    print ("That's all my guesses.")
                    game_on = False
                    try_again = False
                    break
                index =  random.randint(0, len(guesses)-1)  #this needs refactoring to one location
                number = guesses.pop( index )
                if raw_input("I guess {}. Is that what you picked? y or n: ".format(number)) in yes_tuple:
                    if raw_input("I win. Play again? y or n: ") in yes_tuple:
                        guesses = range(1,11)
                        break
                    else:
                        game_on = False
                        try_again = False
                        break
                else:
                    continue
            else:  #Can I guess again?
                if raw_input("Do you want to pick a new number? y or n: ") in yes_tuple:
                    guesses = range(1,11)
                    break
                else:
                    game_on = False
                    try_again = False
                    break
    print("Okay, Good bye.") 

    
if __name__=="__main__":
    main()
