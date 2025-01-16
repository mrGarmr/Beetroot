#Using python as a calculator.

#Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: 

#Addition
#Subtraction
#Division
#Multiplication
#Exponent (Power)
#Modulus
#Floor division

a = int(input('Please, enter first number: '))
b = int(input('Please, enter second number: '))

print(f'Addition: {a+b}')
print(f'Subtraction: {a-b}')
print(f'Division: {a/b}')
print(f'Multiplication: {a*b}')
print(f'Exponent (Power): {a**b}')
print(f'Modulus: a = {abs(a)} and b = {abs(b)}')
print(f'Floor division: {a//b}')

