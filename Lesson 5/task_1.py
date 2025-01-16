#The greatest number

#Write a Python program to get the largest number from a list of random numbers with the length of 10

#Constraints: use only while loop and random module to generate numbers
import random

#Особисто я люблю такі вирази в 1 стрічку:
#data = [random.randint(0,100) for i in range(10)]
data = []
counter = 0

while counter <10:
    data.append(random.randint(0,100))
    counter += 1


#Якщо я правильно зрозумів for item in data... не використовувати, тільки while. Тому так:
maximum_item = data[0]
index_data = 1

while index_data < len(data):
    if data[index_data] > maximum_item:
        maximum_item = data[index_data]
    index_data += 1
print(f'Generated list: {data}')
print(f'Largest number of list: {maximum_item}')

#_-------------------------------------------------------------------------------------------------------------


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

#_-------------------------------------------------------------------------------------------------------------

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



