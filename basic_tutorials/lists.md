Lists
=====

A List is a very useful data structure.  It allows you to hold multiple values / variables together in an organized, ordered way, without giving each of them a separate name.  For example, instead of writing:

	>>> even_number_1 = 2
	>>> even_number_2 = 4
	>>> even_number_3 = 6
	>>> even_number_4 = 8

(Which could get very tedious!)  I can use a List and write:

	>>> even_numbers = [2,4,6,8]

Note:  Lots of other programming languages have something almost exactly like a List, but in most languages it is called an Array.  Even though there's nothing in Python formally called an "Array", you may still hear people refer to Lists as Arrays.


Creating a List
---------------

You can create a List using square brackets.  If you don't put anything in the brackets, it's an empty List.  Don't worry, you can always add things to it later.

	>>> mylist = []

If you want to create a non-empty List, just put any values you want inside the square brackets, separated by commas:

	>>> mylist = [1,1,2,3,5,8]

You can put any kind of value from Python inside your Lists -- numbers, strings -- even other Lists and Dictionaries.

	>>> otherlist = ['you','can','also','have','strings']
	>>> mixedlist = ['and',1,'you','can','mix']
	>>> list_in_list = ['lists','can','go','in','lists',['see?']]


Using the range() function to get a List of numbers
---------------------------------------------------

Python makes it easy to get a List of numbers from say 0-10 without having to type it out by hand or write a special loop to do it.  The range() function does this:

	>>> range(10)
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Notice that it went UP TO 10 but NOT INCLUDING 10!  This is important to understand.  Since it starts at 0, 0-9 is actually 10 numbers.  (0-10 would be 11.)

If you give range() 2 numbers instead of 1, you get a List from A to B instead of just starting at 0:

	>>> range(5,10)
	[5, 6, 7, 8, 9]


Getting an Item in a List
-------------------------

Just like we used square brackets to define a list, we use them to get an Item within a list.  Put the number of which Item you want inside the square brackets.  Remember to start counting at 0, not 1!

	>>> L = ['this','that','the other']
	>>> L[0]
	'this'
	>>> L[1]
	'that'
	>>> L[2]
	'the other'

We can also use negative indexing to grab items starting at the end of our list.  -1 gives you the last item in the list, -2 the 2nd-to-last, and so on:

	>>> L = ['this','that','the other']
	>>> L[-1]
	'the other'
	>>> L[-2]
	'that'



Adding Items to a List
----------------------

You can add an item to the end of a list using .append():

	>>> L = ['one','two']
	>>> L.append('three')
	>>> L
	['one', 'two', 'three']

Or you can insert something at a certain place within the list using .insert().  When you use insert, you have to tell it 2 things: the position where you want to insert (as a number), and then the item that you want to insert.  Inserting at position 0 means at the beginning of the list:

	>>> L.insert(0, 'before')
	>>> L
	['before', 'one', 'two', 'three']

Inserting at position 1 will go in between the 1st 2 items, etc.:

	>>> L.insert(1, 'between')
	>>> L
	['before', 'between', 'one', 'two', 'three']


Getting a Subrange within a List
--------------------------------

Let's say we have this List:

	>>> L = [1,'fish',2,'fish','red','fish','blue','fish']

We can select just a part of this list, a "range", by using square brackets with 2 numbers and a colon between.  The whole List, all 8 elements, would be like this:

	>>> L[0:8]
	[1,'fish',2,'fish','red','fish','blue','fish']

But you could get just the first 6 like this:

	>>> L[0:6]
	[1,'fish',2,'fish','red','fish']

Or just the middle 4 like this:

	>>> L[2:6]
	[2,'fish','red','fish']

Again, notice how whatever number you put second, for example, 6 -- it goes UP TO L[6] but NOT INCLUDING L[6].  I thought that was really weird at first but after programming for a while it ends up making a lot of sense, trust me!  (It's related to the fact that counting starts at 0.)


Lists vs. Dictionaries
----------------------

There's another type of data structure called a Dictionary which also gives us a way to group multiple values and variables together into a single variable.  We'll go into the details of how Dictionaries work, but for now let's talk about the key differences between Lists and Dictionaries:

* __Ordering__ -- The items in a List are kept in the exact order you put them in.  Dictionaries do not let you control what order your items go in.
* __No Names for each Item__ -- The overall List can have a name of course, but each individual Item inside it doesn't have one.  So if you had a list called ShoppingList, the separate items are just ShoppingList[0], ShoppingList[1], etc.  In a Dictionary, you give a name to each Item within the Dictionary.

