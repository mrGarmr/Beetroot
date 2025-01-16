#Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. 
# The function should then print "My favorite movie is named {name}".

def favorite_movie(data):
    return f'My favorite movie is named {data}.'

if __name__ == '__main__':
    print(favorite_movie(input('Enter your favorie movie: \n')))
