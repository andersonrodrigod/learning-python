#List

thislist = ["apple", "banana", "cherry"]
"""

print(thislist)

"""

# List Length

thislist = ["apple", "banana", "cherry"]
"""

print(len(thislist))


"""

# type()

mylist = ["apple", "banana", "cherry"]

"""

print(type(mylist))

"""

# The list() Constructor

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
"""

print(thislist)

"""

# Access Items

thislist = ["apple", "banana", "cherry"]
"""

print(thislist[1])

"""

# Negative Indexing

thislist = ["apple", "banana", "cherry"]

"""

print(thislist[-1])

"""

# Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
"""

print(thislist[2:5])

"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

"""

print(thislist[:4])

"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

"""

print(thislist[2:])

"""

# Range of Negative Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

"""

print(thislist[-4:-1])

"""

# Check if Item Exists

thislist = ["apple", "banana", "cherry"]

"""

    if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
"""

# Change Item Value


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

"""

print(thislist)

"""

# Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]

"""

print(thislist)

"""

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]

"""

print(thislist)

"""

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]

"""

print(thislist)

"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
"""

print(thislist)

"""













