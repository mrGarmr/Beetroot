#Extracting numbers.

#Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

#Constraint: use only while loop for iteration

data = [i for i in range(1,101)]
result = []

index_data = 0

while index_data < len(data):
    if (data[index_data] % 5 != 0 and data[index_data] % 7 == 0) :
        result.append(data[index_data])
    index_data += 1
print(f'All integers from the list that are divisible by 7, but not a multiple of 5: {result}')
