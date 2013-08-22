# Slide 1: Lines

# Each statement ends with a new line

print "Hello, world!"

print "This is another statement"

# Or you can continue a long statement over multiple lines with the \ character

print "hello world, this is a very long statement \
and for the sake of readability I've spread it over \
multiple lines."

# Triple quoted strings, etc

print """
This is a long statement
it can spread as many lines as I want
there's no limit and this could go on all day.
"""

# This is useful for keeping your dictionaries readable, but is not necessary.
emails = {
    'luke':'totallynotarealemail@gmail.com',
    'tom':'examplemail@gmail.com' 
}

print emails['luke']