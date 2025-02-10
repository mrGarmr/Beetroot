# Create your own implementation of a built-in function range, named in_range(), 
# which takes three parameters: 'start', 'end', and optional step. Tips: See the documentation for 'range' function

def in_range(start, end, step=1):
    '''Own implementation of a built-in function range'''

    if step == 0:
        raise ValueError("Step must not be zero")

    cursor = start
    # going up
    if step > 0:
        while cursor < end:
            yield cursor
            cursor += step
    # going down
    else:
        while cursor > end:
            yield cursor
            cursor += step

# for num in range(14, 10, -1):
# 	print(num)
for num in in_range(14, 10, -1):
    print(num)

