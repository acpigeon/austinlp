import random, math

# utility functions to make asking questions easier:

def ask_yes_no_question(question):
    '''ask a yes/no question and keep asking until they say yes or no'''
    while True:
        what_u_say = raw_input(question + ' [y/n] ')
        if what_u_say.lower() in ['y','yes','yeah','uh huh']:
            return True
        elif what_u_say.lower() in ['n','no','naw','nuh uh','nope']:
            return False
        else:
            print "Didn't quite get that!  Answer y or Y or n or N, please!"

def ask_for_number(question):
    '''ask for a number and keep asking until they type a number'''
    while True:
        what_u_say = raw_input(question + ' ')
        try:
            return int(what_u_say)
        except:
            print "Didn't quite get that!  Type a whole number please!"

# main loop for number-guessing game

wanna_play = True
while wanna_play:
    my_number = random.randint(1,10)
    while True:
        your_guess = ask_for_number("I am thinking of a number between 1 and 10.  What's your guess?")
        if your_guess > my_number:
            print "Too high!"
        elif your_guess < my_number:
            print "Too low!"
        elif your_guess == my_number:
            print "Heck yeah, way to go!"
            break
    wanna_play = ask_yes_no_question('Wanna play again?')

print 'K see ya'

