# Task 1

# Write a Python program to detect the number of local variables declared in a function.


def function():
    a = 1
    b = '1'
    c = 3
    f = 3

    result = len(locals())
    
    print(f'In this function we have {result} local variables declared.')
    
    return result

function()
