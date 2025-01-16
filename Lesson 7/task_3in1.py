#Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. 
# The function should then print "My favorite movie is named {name}".

def favorite_movie(data):
    return f'My favorite movie is named {data}.'

if __name__ == '__main__':
    print(favorite_movie(input('Enter your favorie movie: \n')), end='\n\n')

#_----------------------------------------------------------------------------------------------------------------------
print('TASK_2')

#Create a function called make_country, which takes in a country’s name and capital as parameters. 
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. 
# Make the function print out the values of the dictionary to make sure that it works as intended.
result_dict ={}


def dictionary_generator(country, capital):
    result_dict.update({country:capital})
    print(result_dict, end='\n\n')
    return result_dict

if __name__ == '__main__':
    dictionary_generator('Ukraine','Kiev')
    dictionary_generator('Germany','Berlin')
    #dictionary_generator(input('Enter country: \n'),input('Enter capital: \n'))

#_----------------------------------------------------------------------------------------------------------------------

print('TASK_3')

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