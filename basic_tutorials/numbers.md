# Numbers

[Official Python Docs](http://docs.python.org/2/tutorial/introduction.html#numbers)

Python handles math and numbers in a very logical manner and is similar to many other programming languages.

Addition is done with the + symbol.

	# Add 2 and 2
	>>>> 2+2
	4

Subtraction is done with the - symbol.

	# Subtract 2 from 4
	>>>> 4-2
	2

Multiplication is done with the * symbol.

	# Multiply 2 and 4
	>>>> 2*4
	8

Division is done with the / symbol. The difference between integers and floating point numbers is significant in python. Division of two integers returns the floor. Floating point is simple as well.

	# Divide 8 by 2
	>>>> 8/2
	4

	# Divide 8.0 by 3.2
	>>>> 8.0/3.2
	2.5

	# Divide 8 by 3
	>>>> 8/3
	2

The last example shows how python handles dividing two integers. Python returns the nearest integer rounded down. To get a more precise value convert to floating point.

	# Get a more precise version of 8/3
	>>>> 8.0/3
	2.6666666666666665

The modulus operator return the remainder of two numbers.

	# Get the remainder of 10/4
	>>>> 10%4
	2

Python is capable of handling very advanced mathematics. Documentation can be found in the [Python Tutorial](http://docs.python.org/2/tutorial/introduction.html#numbers) and more advanced math can be done with the [math module](http://docs.python.org/2/library/math.html).