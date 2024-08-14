import re


# RegEx in Python


txt = "The rain in Spain"
a = re.search("^The.*Spain$", txt)

if a:
 ''' print("YES! We have a match!")'''
else:
 ''' print("No match")'''




# The findall() Function

txt = "The rain in Spain"
x = re.findall("ai", txt)
'''print(x)'''


txt = "The rain in Spain"
x = re.findall("Portugal", txt)
'''print(x)'''

# The search() Function

txt = "The rain in Spain"
x = re.search("\s", txt)

'''print("The first white-space character is located in position:", x.start()) '''

txt = "The rain in Spain"
x = re.search("Portugal", txt)
'''print(x)'''

# The split() Function

txt = "The rain in Spain"
x = re.split("\s", txt)
'''print(x)'''


txt = "The rain in Spain"
x = re.split("\s", txt, 1)
'''print(x)'''


# The sub() Function


txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
'''print(x)'''


txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
'''print(x)'''


# Match Object

txt = "The rain in Spain"
x = re.search("ai", txt)
'''print(x)
'''

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
'''print(x.span())'''

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
'''print(x.string)'''

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())