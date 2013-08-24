# 5: Numeric Literals

#cmath is used for performing operations on complex numbers
import cmath

# integer
value = 192

# boolean, and floating point

# True
if value > 3.148:
    print "That's a big number!"
# False
else:
    print "That's not a very big number!"

# Complex numbers, don't ask me for the fine points of these.
wat = cmath.sin(2 + 5j)
print wat