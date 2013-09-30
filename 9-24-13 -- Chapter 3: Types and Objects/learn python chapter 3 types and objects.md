Austin Learn Python  
Tuesday, September 23, 2013  
Ryan Murphy

![image](python.png)

# Types and Objects (Chapter 3 in the book) #

An object is a structure that can store data and perform predefined behaviors on that data.
Every variable we define in our Python programs is an object.
We can design custom objects with custom behaviors by defining a Class.


### Type and Value ###Each object has
* a type (a.k.a. its class)
* a value

For example, if we say _x = 5_, we are creating an object with type _int_ (short for integer) and value _5_.

When an object of a particular type or class is created, that object is sometimes called an instance of that type.

You can check an object's type with the _type()_ and _isinstance()_ functions:

	(in interactive interpreter)
	>>> x = 3
	>>> x
	3
	>>> type(x)
	<type 'int'>
	>>> isinstance(x,int)
	True
	>>> isinstance(x,str)
	False

### Attributes and Methods ###

Attributes and methods are accessed using the dot (.) operator:

	(pure python code, no interactive interpreter)
	a = 3 + 4j				# Create a complex number (an object of type "complex")	r = a.real				# Get the real part (an attribute)	b = [1, 2, 3]			# Create a list (an object of type "list")	b.append(7)				# Add a new element using the append method


### Mutable and Immutable ###

If an object’s value can be modified, the object is said to be mutable. If the value cannot be modified, the object is said to be immutable.

Example -- lists are mutable, you can change them after you've defined one…

	>>> evens = [1,4,6,8]
	>>> evens[0] = 2
	>>> evens
	[2, 4, 6, 8]

But strings are immutable, once you've defined one you can't make changes:

	>>> hello = "hi"
	>>> hello[0] = 'j'
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'str' object does not support item assignment

### References and Copies ###

### First-Class Objects ###

### Built-in Types for Representing Data ###

#### The None Type
* returned by functions that don't explicitly return a value
* doesn't show up if returned by interpreter:

#### Numeric Types

* int and long
* float and complex

#### Sequence Types
* e.g. lists, tuples, strings
* can be referenced by index: `s[i], s[i:j], s[i:j:stride]`
* each sequence _s_ has `len(s), min(s), max(s), sum(s), all(s), any(s)`
* mutable sequences have `s[i] = v, s[i:j] = L, del s[i], del s[i:j]`
* lists have `s.append(v), s.extend(L), s.count(v), s.index(v), s.insert(i,x), reverse, sort, …`

##### Strings

String.format() example (easy way to do a "fill-in-the-blank" using a string):

	>>> a = "Your name is {0} and your age is {age}"
	>>> a.format("Mike", age=40)	'Your name is Mike and your age is 40'

Strings have `s.capitalize(), s.center(width[, pad]), s.count(sub), s.decode() s.encode(), s.expandtabs([tabsize]), s.find(sub), s.split(sep), s.title()`, and much more.


#### Mapping Types

* e.g. Dictionaries
* Dictionaries have `len(D), D[k], D[k]=x, del D[k], k in D, D.clear(), D.copy(), D.get(s [, value]), D.items(), D.keys(), D.values(), D.setdefault(k [, default]), D.update(dict2)`


#### Set Types

	s = set([1,5,10,15])
	f = frozenset(['a',37,'hello'])

* Sets have `len(s), s.copy(), s.difference(t), s.intersection(t), s.isdisjoint(t), s.issubset(t), s.issuperset(t), s.symmetric_difference(t), s.union(t)`
* Mutable sets have `s.add(item), s.clear(), s.difference_update(t), s.discard(item), s.intersection_update(t), s.pop(), s.remove(item), s.symmetric_difference_update(t), s.update(t)`

### Built-in Types for Representing Program Structure ###
#### Callable Types
* Functions
* Methods
* Classes as callables -- the constructor `__init__`
* Instances as callables -- the `__call__` method

#### Classes, Types, and Instances
#### Modules

### Built-in Types for Interpreter Internals ###
* Code Objects
* Frame Objects
* Traceback Objects
* Generator Objects
* Slice Objects
* Ellipsis Object

### Object Behavior and Special Methods ###
* Object Creation and Destruction
* Object String Representation
* Object Comparison and Ordering
* Type Checking
* Attribute Access
* Attribute Wrapping and Descriptors
* Sequence and Mapping Methods
* Iteration
* Mathematical Operations
* Callable Interface
* Context Management Protocol
* Object Inspection and dir()



## Extra Info / "Under the Hood" ##

This is not necessary to know to use Python, but it is interesting to know how things work "under the hood", and could be useful in some cases.

### An Object's Identity Number ###

Each object has a special number called the identity, which is often the location where the object is stored in memory.

The built-in function id() returns the identity of an object as an integer:

	>>> x = 5
	>>> id(x)
	140611864822120

### Reference Counting and Garbage Collection ###
