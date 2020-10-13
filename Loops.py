# Conditions and If statements
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 10
b = 20
c = 15
d = 20
if b < a:
    print("b is greater than a")
else:
    print("b is greater than a")
if c > b:
    print("b is less than c")
elif b == d:
    print("b and d are equal")
# Short Hand if else
print("a") if a > b else print("b")
if a < b and c > a:
  print("Both conditions are True")
print('\n')

# pass Statement
# some reason have an if statement with no content
# put in the pass statement to avoid getting an error
a = 33
b = 200

if b > a:
  pass
print('\n')
print('\n')
# Loops
# two primitive loop 1. while loop, 2. for loop
# While loop
# execute set of statements as long as a condition is true
i = 1
while i < 6:
  print(i)
  i += 1

# Break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print('\n')
# continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# Print a message once the condition is false
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
print('\n')

# For Loops
# iterating over a sequence (a list, a tuple, a dictionary, a set, or a string)
place = ["Bangalore", "Chennai", "Salem"]
for x in place:
  print(x)
print('\n')

# print each char in a String
for x in "banana":
  print(x)
print('\n')

# break Statement
place = ["Bangalore", "Chennai", "Salem"]
for x in place:
  print(x)
  if x == "Chennai":
    break
print('\n')

# continue Statement
place = ["Bangalore", "Chennai", "Salem"]
for x in place:
  if x == "Chennai":
    continue
  print(x)
print('\n')

# The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number.

for x in range(10):
  print(x)

for x in range(2, 30, 3):
  print(x)
print('\n')

state = ["KA", "TN", "TN"]
place = ["Bangalore", "Chennai", "Salem"]

for x in state:
  for y in place:
    print(x, y)
print('\n')
# pass Statement
for x in [0, 1, 2]:
  pass
print('\n')

# Iterators
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)