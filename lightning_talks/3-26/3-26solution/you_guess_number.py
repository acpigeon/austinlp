# -*- coding: utf-8 -*-
#You guess the computer's number
"""
>>> python you_guess_number.py

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
    change the output of the program so that it could be used as the logic in a web page
"""
import random
print ("Welcome")
play_again = True
new_number = True
while play_again == True:
    if new_number == True:
        num = random.randint(1, 10)
    new_number = True 
    g = input( "Guess a number between 0 and 10: ")
    guess = int(g)
    if guess == num:
        print ("You win. You guessed {}, the correct number".format(guess) )
        again = raw_input("Play again? y or n: ")
    elif guess < num:   
        print ("You missed. You guessed {}, but the number was higher.".format(guess) )    
        again = raw_input("Play again? y or n: ")
        if again=='y':
            new_number = True if raw_input("With a new number? y or n: ")=='y' else False        
    elif guess > num:
        print ("You missed. You guessed {}, but the number was lower.".format(guess) )    
        again = raw_input("Play again? y or n:")
        if again=='y':
            new_number = True if raw_input("With a new number? y or n: ")=='y' else False
    else:
        print("Don't you want to play?")
        again = raw_input("Play again? y or n:")
    if again=="y":
        play_again = True
    else:
        play_again = False
    
print "Good bye"