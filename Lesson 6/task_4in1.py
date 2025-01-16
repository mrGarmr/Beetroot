#Task 1
#Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.

data = input(f'Please, enter your sentence: \n').split(' ')
print(data)
#sentence_dict = {element : data.count(element) for element in data}

sentence_dict = {}

for element in data:
    sentence_dict.update({element : data.count(element)})

print(sentence_dict)

print('---------------------------------------------------------------------------------------------------------------------')

#---------------------------------------------------------------------------------------------------------------------
#Task 2

#Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the quantity of this exact item.

#The code has to return the dictionary with the sums of the prices by the goods types.

#Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
#sums_goods = { element : (stock[element]*prices[element]) for element in stock.keys()}

sums_goods = {}

for fruit in stock.keys():
    sums_goods.update({fruit : stock[fruit] * prices.get(fruit)})

print(sums_goods)
print('---------------------------------------------------------------------------------------------------------------------')

#---------------------------------------------------------------------------------------------------------------------
#Task 3

#List comprehension exercise

#Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.

print([(item,item**2) for item in range(1,11)])
print('---------------------------------------------------------------------------------------------------------------------')

#---------------------------------------------------------------------------------------------------------------------
#Task 4

#Створити лист із днями тижня.
#В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
#Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

first_dict = {element: days.index(element)+1 for element in days}
print(first_dict)

second_dict = {days.index(element)+1 : element for element in days}
print(second_dict)
#---------------------------------------------------------------------------------------------------------------------