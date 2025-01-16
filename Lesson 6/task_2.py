
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