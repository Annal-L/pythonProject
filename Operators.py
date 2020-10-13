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

# Assignment operators
a = 3
temp = 18
temp += a # Using += Operator
print("The Value of the temp after using += Operator is: ", temp )
temp -= a # Using -= Operator
print("The Value of the temp after using -= Operator is: ", temp )
temp *= a # Using *= Operator
print("The Value of the temp after using *= Operator is: ", temp )
temp //= a # Using //= Operator
print("The Value of the temp after using //= Operator is: ", temp )
temp **= a # Using **= Operator
print("The Value of the temp after using **= Operator is: ", temp )
temp /= a # Using /= Operator
print("The Value of the temp after using /= Operator is: ", temp )
temp %= a # Using %= Operator
print("The Value of the temp after using %= Operator is: ", temp )
x = 5
y = 12
x &= y # Using &= Operator
print("The Value of the x after using &= Operator is: ", x)
x |= 9 # Using |= Operator
print("The Value of the x after using |= Operator is: ", x)
x ^= y # Using ^= Operator
print("The Value of the x after using ^= Operator is: ", x)
print('\n')

# Comparison operators
x = 14
y = 16

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)
print('\n')

# Comparison operators
if 1 < 2 and 4 > 2:
 print("condition true")

if 1 > 2 and 4 > 10:
 print("condition false")

if 4 < 10 or 1 < 2:
 print("condition true")

x = False
if not x :
    print("condition met")
else:
    print("condition not met")
print('\n')

# Identity Operators
# compare the objects,

x = ["Pen", "Pencil"]
y = ["Pen", "Pencil"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y,
# even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is"
# and "==": this comparison returns True
# because x is equal to y
print('\n')

# Membership Operators
# in , not in
# test if a sequence is presented in an object
x = ["Pen", "Pencil"]
print("eraser" not in x)
print('\n')

# Bitwise Operators
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b;        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)
print('\n')