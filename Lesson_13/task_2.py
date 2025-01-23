# Task 2

# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def numbers(a, b):
    
    def add():
        
        result = a+b
        
        return f'The sum of two numbers: {result}'

    return add()

print(numbers(3,5))
