# Open a File on the Server

'''f = open("demofile.txt", "r")
print(f.read())
'''
f = open("./files/demofile.txt", "r") # in same folder
'''print(f.read())'''


# Read Only Parts of the File
'''print(f.read(5))'''


# Read Lines
'''print(f.readline())
print(f.readline())''' # two first lines

'''for x in f:
  print(x)'''


# Close Files

print(f.readline())
f.close()

# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.





