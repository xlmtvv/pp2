print("Hello")
print('Hello')

a = "Hello"
print(a)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


a = "Hello, World!"
print(a[1])


for x in "banana":
  print(x)


a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)


b = "Hello, World!"
print(b[2:5])


a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


txt = "We are the so-called \"Vikings\" from the north."




# Exercise 1
x = "Hello World"
print(len(x))

# Exercise 2
txt = "Hello World"
x = txt[0]

# Exercise 3
txt = "Hello World"
x = txt[2:5]

# Exercise 4
txt = " Hello World "
x = txt.strip()

# Exercise 5
txt = "Hello World"
txt = txt.upper()

# Exercise 6
txt = "Hello World"
txt = txt.lower()

# Exercise 7
txt = "Hello World"
txt = txt.replace('H', 'J')

# Exercise 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
