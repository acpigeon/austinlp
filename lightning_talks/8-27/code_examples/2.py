# slide 2: Indentation

class MyClass:
    """This is a docstring, it explains your class"""
    def userEnteredName(name):
        if name:
            print "Hello, " + name
        else:
            print "Hello, user."

    name = raw_input("Your name, please: \n")

    userEnteredName(name)

if __name__ == "__main__":
    MyClass()