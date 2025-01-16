#Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.

data = input(f'Please, enter your sentence: \n').split(' ')
print(data)
#sentence_dict = {el : data.count(el) for el in data}

sentence_dict = {}

for element in data:
    sentence_dict.update({element : data.count(element)})

print(sentence_dict)