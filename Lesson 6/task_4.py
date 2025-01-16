#Створити лист із днями тижня.
#В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
#Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

first_dict = {element: days.index(element)+1 for element in days}
print(first_dict)

second_dict = {days.index(element)+1 : element for element in days}
print(second_dict)