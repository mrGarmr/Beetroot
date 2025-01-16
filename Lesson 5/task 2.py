#Exclusive common numbers.

#Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.

#Constraints: use only while loop and random module to generate numbers

import random

data_1 = []
data_2 = []
data_3 = []
counter = 0

while counter <10:
    data_1.append(random.randint(0,10))
    data_2.append(random.randint(0,10))
    counter += 1
    
print(f'Generated list #1: {data_1}')
data_1 = list(set(data_1))
index_data = 0

while index_data < len(data_1):
    if data_1[index_data] in data_2:
        data_3.append(data_1[index_data])
    index_data += 1


print(f'Generated list #2: {data_2}')
print(f'The common digets: {data_3}')