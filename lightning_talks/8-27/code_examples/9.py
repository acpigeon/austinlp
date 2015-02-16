# 9: Docstrings

def hello(user):
	"""This function prints "Hello, " followed by the users name"""
	print "Hello, " + user

if __name__ == "__main__":
	print hello.__doc__
	user = "Luke"
	hello(user)