# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter 
# (to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) as the second parameter. 
# Then return the sum or product of all the numbers in the arbitrary parameter. For example:

# the call make_operation('+', 7, 7, 2) should return 16
# the call make_operation('-', 5, 5, -10, -20) should return 30
# the call make_operation('*', 7, 6) should return 42  

def add(operands):
    result = int(operands[0])
    for i in operands[1:]:
        result += int(i)
    return result

def make_operation(operator, *operands):   
    calculate = {
        '+': add(operands),
        '-': minus(operands),
        '*': multiply(operands)
    }
    print(f'The answer is: {calculate[operator]}')

def minus(operands):
    result = int(operands[0])
    for i in operands[1:]:
        result -= int(i)
    return result

def multiply(operands):
    result = int(operands[0])
    for i in operands[1:]:
        result *= int(i)
    return result

if __name__ == '__main__':
    make_operation('+', 7, 7, 2)
    #make_operation('-', 5, 5, -10, -20)
    #make_operation('*', 7, 6)