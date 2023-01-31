"""
x = y = z = "Orange"
print(x)
print(y)
print(z)
"""
"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
"""
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""
"""
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
"""
"""
x = 5
y = "John"
print(x , y)
"""
"""
x = "awesome"
def comment():
  print("Python is " + x)
comment()
print("Python is " + x)
"""
"""
def myfunc():
  global x
  x = "fantastic"
myfunc()
print(x)
"""
"""
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
"""

#  DATA TYPES
"""
Text Type:---	str
Numeric Types:---	int, float, complex
Sequence Types:---	list, tuple, range
Mapping Type:---	dict
Set Types:---	set, frozenset
Boolean Type:---	bool
Binary Types:---	bytes, bytearray, memoryview
None Type:---	NoneType
"""

"""
Example	             Data Type	     
x = "Hello World"---	str
x = 20---	int
x = 20.5---	float
x = 1j---	complex
x = ["apple", "banana", "cherry"]---	list
x = ("apple", "banana", "cherry")---	tuple
x = range(6)---	range
x = {"name" : "John", "age" : 36} ---	dict
x = {"apple", "banana", "cherry"} ---	set
x = frozenset({"apple", "banana", "cherry"}) ---	frozenset
x = True----	bool
x = b"Hello"----	bytes
x = bytearray(5)----	bytearray
x = memoryview(bytes(5))----	memoryview
x = None--- 	NoneType
"""
"""
import random
print(random.randrange(1, 20))
"""
"""
txt = "The best things in life are free!"
print("free" in txt)
"""
"""
txt = "The best things in life are free!"
if "get" not in txt:
    print("yes am absent")
 """
"""
#slicing
b = "Hello, World!"
print(b[:5])
print(b[1:5])
print(b[1:])
print(b[-6:])
    """
"""
a = "Hello, World!"
print(a.replace("Hello", "Jjombwe's"))
    """
"""
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] as long as there is a comma
   """
"""
a = "Hello"
b = "World"
c = a +' '+ b
print(c)
"""
"""
a = 36
c = 80
b = "My name is John, I am {1} and my brother {0}"
print(b.format(a,c))
"""
"""
txt = 'We are the so-called \'Vikings\' from the north.'
print(txt)
"""

"""
def myFunction() :
  return False

print(myFunction())
"""
"""
def name():
    return False

if name():
    print('yes!')
else:
    print('No')
"""
"""
x = 200.7
print(isinstance(x,complex))
"""

"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is not y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
"""