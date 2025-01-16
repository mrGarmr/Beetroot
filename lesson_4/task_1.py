# The Guessing Game.

# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
# The result should be sent back to the user via a print statement.

import random

random_number = random.randrange(1, 10)
guess_quantity = 3
print('You have three posibility to guess the number. ')

while guess_quantity:
    answear = input(f'Your {"first" if guess_quantity==3 else "second" if guess_quantity ==  2 else 'last' } try. What is your number? \n')
    
    if answear.isdigit():
        if int(answear) == random_number:
            print('CONGRATULATIONS!!! You are right and win!')
            break

        elif guess_quantity == 1:
            guess_quantity -= 1
            print(f'Sorry you lost the GAME. The right number was: {random_number}')

        else:
            print(f'Sorry, you are wrong. {"The number is higher." if int(answear) < random_number else "The number is lower."}')
            guess_quantity -= 1

    else:
        print('Please, enter your answear with digets.')

