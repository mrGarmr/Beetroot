# Create your own implementation of a built-in function enumerate, named 'with_index', 
# which takes two parameters: 'iterable' and 'start', default is 0. 
# Tips: see the documentation for the enumerate function

def with_index(iterable, start=0):
    '''Implementation of a built-in function enumerate'''
    index = start
    
    for item in iterable:
        yield index, item
        index += 1

items = ['bread', 'milk', 'butter'] 

for index, item in with_index(items, start=1):
    print(f"Index: {index}, Item: {item}")