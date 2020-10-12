# Creating Variables
# swap two values without using third variable
a = 25
b = 30
b = b - a
a = a + b
b = b + b
print("swap two values : ")
print(a)
print(b)
print('\n')

# Multiple Variables
a, b, c = "Apple", "Banana", "Cherry"
print("multiple Variables : ")
print(a)
print(b)
print(c)
print('\n')

# Example of Global Variable
a = 1
# Example of Local Variable
def sample():
# Local Variable
 a = 1


# Arithmetic operations
n1 = int(input('Enter First number: '))
n2 = int(input('Enter Second number '))
add = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
floor_div = n1 // n2
power = n1 ** n2
modulus = n1 % n2
print('Addition of ',n1 ,'and' ,n2 ,'is :',add)
print('Subtraction of ',n1 ,'and' ,n2 ,'is :',sub)
print('Multiplication of' ,n1 ,'and' ,n2 ,'is :',mul)
print('Division of ',n1 ,'and' ,n2 ,'is :',div)
print('Floor Division of ',n1 ,'and' ,n2 ,'is :',floor_div)
print('Exponent of ',n1 ,'and' ,n2 ,'is :',power)
print('Modulus of ',n1 ,'and' ,n2 ,'is :',modulus)
print('\n')

# same value to multiple variables in one line
x = y = z = "Python"
print(x)
print(y)
print(z)
print('\n')

# + character to add a variable to another variable
x = "Python is "
y = "awesome"
z = x + y
print(z)
print('\n')

# Global variable with my function
x = "Python"

def myfunc():
 x = "fantastic"
 print("Python is " + x)

myfunc()
print(x + " is awesome")

# Numbers: Convert from one type to another
x = 10   # int
y = 2.9  # float
z = 5j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
print('\n')

# Type casting
a = int(2)   # a will be 2
b = int(9.8) # b will be 9
c = int("7") # c will be 7

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

i = str("s1") # i will be 's1'
j = str(2)    # j will be '2'
k = str(3.0)  # k will be '3.0'
