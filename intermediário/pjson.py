import json


# Parse JSON - Convert from JSON to Python

# some JSON:
#x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
'''y = json.loads(x)'''

# the result is a Python dictionary:
'''print(y["age"])'''


# Convert from Python to JSON

# a Python object (dict):
a = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
b = json.dumps(a)

# the result is a JSON string:
print(b)


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

'''print(json.dumps(x))'''

# use four indents to make it easier to read the result:

'''print(json.dumps(x, indent=4))'''


# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:

'''print(json.dumps(x, indent=4, separators=(". ", " = ")))'''

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
