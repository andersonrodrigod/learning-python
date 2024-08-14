x = 5   # x is of type int
y = "Rodrigo" # x is now of type str

# variables datatype

a = str(3) # a will be '3'
b = int(3) # b will be 3
c = float(3) # c will be 3.0

"""

print(type(x))
print(type(y))

"""

# One Value to Multiple Variables

x, y, z = "orange", "banana", "cherry"

"""

print(x)
print(y)
print(x)

"""

# One Value to Multiple Variables

x = y = z = "orange"
"""
print(x)
print(y)
print(x)

"""
 
# Unpack a Collection

fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

"""

print(x)
print(y)
print(z)

"""

# Output Variables

x = "Python is awesome"

"""

print(x)

"""

x = "Python"
y = "is"
z = "awesome"

"""

print(x, y, z)

"""

x = "Python "
y = "is "
z = "awesome"

"""

print(x + y + z)

"""


x = 5
y = 10

"""

print(x + y)

"""

# Global Variables

x = "awesome"

def myfunction():
    print('python is ' + x)

"""

myfunction()

"""


x = "awesome"

def myfunc():
    x = "fantastic"
    print('python is', x)


"""

myfunc()

print('python is', x)

"""


# The global Keyword


def myfunction():
    global x
    x = "fantastic"

"""

myfunction()

print("Python is", x)

"""
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)