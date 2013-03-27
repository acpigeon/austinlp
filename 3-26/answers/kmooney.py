import random


class InvalidInput(Exception):
    pass


def evaluate_input(user_input, truthy_items, falsy_items):
    if user_input in truthy_items:
        return True
    if user_input in falsy_items:
        return False
    raise InvalidInput("This is invalid input!")


def check_integer(user_input):
    try:
        i = int(user_input)
    except ValueError:
        raise InvalidInput("This is not an integer!")
    return i

guessable_number = random.randint(0, 10)
found_it = False

while not found_it:
    print "What's my number?"
    guessing = True
    while guessing:
        try:
            human_guess = raw_input()
            human_int = check_integer(human_guess)
            guessing = False
        except InvalidInput as ii:
            print ii

    if human_int != guessable_number:
        print "You Lose."
        if human_int < guessable_number:
            print "My Number is higher"
        else:
            print "My Number is lower!"
    else:
        print "You got it!"
        found_it = True
        print "Guess Again? y / n"
        guessing = True
        while guessing:
            try:
                human_response = raw_input()
                if evaluate_input(
                    human_response,
                    ['y', 'Y', 'Yes'],
                    ['n', 'N', 'No']
                ):
                    guessable_number = random.randint(0, 10)
                    found_it = False
                guessing = False
            except InvalidInput as ii:
                print ii
