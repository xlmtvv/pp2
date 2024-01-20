x = 5
y = "John"
print(x)
print(y)

x = "John"
# is the same as
x = 'John'


x = 5
y = "John"
print(type(x))
print(type(y))

a = 4
A = "Sally"
#A will not overwrite a


myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


x = y = z = "Orange"
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# Exercise 1
carname = "Volvo"

# Exercise 2
x = 50

# Exercise 3
x = 5
y = 10
print(x + y)

# Exercise 4
x = 5
y = 10
z = x + y
print(z)

# Exercise 5
x, y, z = "Orange", "Banana", "Cherry"

# Exercise 6
x = y = z = "Orange"

# Exercise 7
def myfunc():
    global x
    x = "fantastic"