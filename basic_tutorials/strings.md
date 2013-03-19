Strings
=======

Strings are basically "Text Messages".  A string is basically a list/array of letters, aka characters.  To tell Python you want to spell out a string, make sure you put quotes ('' or "") around the letters of your String / Text Message.


Counting Letters Within Strings
-------------------------------

Let's say we have a variable called hello that contains the String "hello world":

	>>> hello = "hello world"

We can count the number of occurrences of a certain letter with the count function:

	>>> hello.count('h')
	1
	>>> hello.count('l')
	3

Adding Strings Together
-----------------------

Strings can be added / appended / concatenated to one another:

	>>> 'hello' + 'goodbye'
	'hellogoodbye'

Notice there's no space.  Let's try adding a space in there:

	>>> 'hello' + ' ' + 'goodbye'
	'hello goodbye'

Notice that every time I want to spell out a String, I have to put quotes '' around the letters/characters.
It's ok to use single quotes '' or double quotes "", both can create a String.
(But if you start with a single quote you have to end with a single quote, etc!)

Other things to do with Strings...


Searching Through Strings
-------------------------

Well, any Web Page / HTML file, or any Code File, or any Text File, those are all really just Strings.
The whole file is just one giant list of letter / characters.
So you can imagine that if you wanted to write software to edit such files or display them in a web browser, or do pattern matching on them / search through them, you would want to know how to search within a String.
In Python, we can search through a String using the "search" method:

	>>> 'hello'.find('o')
	4

Notice it says 4.  If I take this "hello" string and start at the beginning of it,
	(making sure to count the very beginning slot as 0, not as 1!)
	"h" is at 0, "e" is at 1, "l" is at 2, other "l" is at 3, and "o" is at 4, see?  So that's what the 4 means.

We can go the other way, to, say 'hello'[4] and get the 'o':


Getting a Letter of a String Based on Where it is in that String
----------------------------------------------------------------

Any string I have, I can say 'that string'[0] and it's gonna give me the first letter.

	# Aside
	# Remember, it always starts at 0, not at 1!  Computers are crazy like that!
	# But they would say we're the crazy ones for starting at 1.
	# I think we only start at 1 because we started counting before we discovered 0, and then we never fully switched over.
	# But good luck making a computer with no concept of 0.

So 'hello'[0] gives me 'h', 'hello'[1] gives me 'e', etc...

If you want the last letter, Python has a shortcut for that too, you can use -1.

'hello'[-1] gives you 'o', just like if you said 4.

	# We could go on and talk about ranges, etc.


Printing out a String to the Screen
-----------------------------------

When we are in the Interactive Interpreter, where the >>> is, and we get to type each line and see the result immediately, we might be confused why there would be any need to "print out" a String or other Variable.  But imagine if we took the same code we are writing line by line, and put all the lines into a File, and the ran the file.  Now we wouldn't see any >>> or any specific explanation of each line, all we would see is exactly what our code tells Python to do.  So then if we want to see any results on the screen, we have to Print them, hence the "print" statement:

	>>> print('hello world')
	hello world

Notice when it prints it the quotes are gone.  Just because we need quotes around a String when we're writing Code, that doesn't mean that the String itself has quotes when you print it out.  It's just the pure Text Message of what you put inside.


Turning a String into a List
----------------------------

We're going to talk about lists a little later on, but for right now I wanted to show you that you could turn a String into a List very easily:

	>>> list('hello world')
	['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

Check it out, it split it apart into its separate letters / characters!  It used to be a String / Text Message, but now it's just being treated as a List of separate Characters, so it no longer shows like a continuous message.

We'll learn more about Lists and what we can do with them a little later on.  For now, let's look at a very important concept in any programming language, (and even in human language!): VARIABLES.

