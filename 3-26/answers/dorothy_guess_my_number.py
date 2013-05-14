import random
import math
game_number = random.randint(1,10)
play_game = 'y'
guess_again = ''
def main():
    welcome()
    number_for_game()
    get_correct_number()
    end_of_game()

def get_correct_number():
    global guess_again
    global play_game
    
    while  play_game.lower() == 'y':
        while True:
            try:
                player_number = raw_input("What's my number? ")
                player_number = int(player_number)
                break
            except ValueError:
                print("Not a valid number! Please try again ...")

        if player_number > 10:
            print
            print "The game highest number is 10"
            print "pick a number less than or equal to 10"
            print

        elif player_number == game_number:
            print
            print "You are a Winner!!"
            print "Your number:", player_number
            print "My number:", game_number
            print "It's a prefect match"
            print "Game Over"
            print
            print
            welcome()
            number_for_game()
            
        elif player_number > game_number:
            
            print "You lose"
            print "My number is smaller"
            print
            get_another_number()     
                    
        else:
            print "You lose"
            print "My number is Larger"
            print
            get_another_number()
                        
                    
def end_of_game():
    global play_game               
    if play_game.lower() == 'n':
        print "Thanks for playing, lets play again sometimes"
    else:
        print "You did not enter y or n"
        print "please try again"
        main()
        
def get_another_number():
    global guess_again
    guess_again = raw_input("Guess again? y or n:  ")
    compare_guess_again()

def compare_guess_again():
    global guess_again
    global play_game
    if guess_again.lower() == "y":
        get_correct_number()
    elif guess_again.lower() == "n":
        play_game = "n"
        return play_game
       
    else:
        wrong_letter()
    
def wrong_letter():
    print
    print "You did not enter y or n"
    print "please try again.."
    print
    get_another_number()   
      
def welcome():
    global play_game
    play_game = raw_input("Hello, would you like to guess my number? Enter y or n:  ")
    return play_game

def number_for_game():
    global game_number
    game_number = random.randint(1,10)
    return game_number
                
    
main()
