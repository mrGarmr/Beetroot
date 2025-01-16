#Create a function called make_country, which takes in a country’s name and capital as parameters. 
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. 
# Make the function print out the values of the dictionary to make sure that it works as intended.
result_dict ={}


def dictionary_generator(country, capital):
    result_dict.update({country:capital})
    print(result_dict)
    return result_dict

if __name__ == '__main__':
    dictionary_generator('Ukraine','Kiev')
    dictionary_generator('Germany','Berlin')
    #dictionary_generator(input('Enter country: \n'),input('Enter capital: \n'))