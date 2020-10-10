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