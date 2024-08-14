# Global Keyword

def myfunc():
  global x
  x = 300

myfunc()

print(x)


# Nonlocal Keyword

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())