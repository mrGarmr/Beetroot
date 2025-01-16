#Write a function called oops that explicitly raises an IndexError exception when called. 
# Then write another function that calls oops inside a try/except state­ment to catch the error. 
# What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    raise IndexError

def test_oops():
    n= ['a', 'b']

    try:
        print(n[2])
    except IndexError:
        oops()
        
test_oops()
         
#If we change oops to KeyError exception wont catch IndexError

#__________________________________________________________________________________

#Write a function that takes in two numbers from the user via input(), call the numbers a and b, 
# and then returns the value of squared a divided by b, construct a try-except block which catches an exception 
# if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).    

def math_value(a, b):
    try:
        result = (int(a)**2)/int(b)
    except ZeroDivisionError:
        print('We cannot divide by Zero')
    except ValueError:
        print('Both input must be number')

    return result

if __name__ == '__main__':
    print(f'\nThe result of equation: {math_value(input(f'Please, enter first number: '),
                                                input(f'\nPlease, enter second number: '))}')