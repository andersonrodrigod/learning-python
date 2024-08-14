# Use a Module
import mymodule


'''mymodule.greeting("Jonathan")'''

a = mymodule.person1['age']
'''print(a)'''

# Re-naming a Module

import mymodule as mx

'''mx.greeting("Jonathan")'''

a = mx.person1['age']
'''print(a)'''


# Built-in Modules

import platform
x = platform.system()
'''print(x)'''


# Using the dir() Function

x = dir(platform)
'''print(x)'''


# Import From Module

from mymodule import person1

print (person1["age"])








