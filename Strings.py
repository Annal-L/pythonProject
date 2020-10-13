# String Literals
# assign string to a variable
a = "Hello"
print(a)
# multiline strings
a = """Python is a general-purpose programming language, 
so it can be used for many things.."""
print(a)
# three single quotes
a = ''' Python is used for web development, 
AI, machine learning, operating systems, 
mobile application development, and video games.'''
print(a)

# String Array
# character at position 1
a = "Beautiful sky"
print("Character at position 1" + a[1])

# Slicing
# return a range of characters by using the slice syntax
b = "Beautiful sky"
print("Range of characters" + b[2:5])

# Negative Indexing
# slice from the end of the string
b = "Hello, World!"
print(b[-5:-2])

# Length
# length of a string, len() function
a = "Beautiful star!"
print(len(a))

# String manipulation
# strip() method removes any whitespace from the beginning or the end
a = " Learning python "
print(a.strip())

# lower() method returns the string in lower case
a = " Learning PYTHON "
print(a.lower())

# upper() method returns the string in upper case
print(a.upper())

# replace() method replaces a string with another string
print(a.replace("PYTHON", "JAVA"))

# split() method splits the string into substring
a = "I am in an interview"
print(a.split(" "))

# check string
b = "Pain is an abstract noun as well as a verb but Paining is no word."
searchtxt = "ain" in b
print(searchtxt)
# NOT present
searchtxt = "ain" not in b
print(searchtxt)

# String Concatenation
# To concatenate, or combine, two strings using this + operator
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String format
# combine strings and numbers by using the format() method
age = 52
txt = "My name is Lin, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 321
price = 12.93
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# use index numbers {0}
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character
# insert characters that are illegal in a string, use an escape character
sampletxt = "Pain is an abstract noun as well as a verb but \"Paining\" is no word."
print(sampletxt)
