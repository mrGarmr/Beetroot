#The math quiz program.

#Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
#and then responds with a message accordingly.
import random

first_number = random.randrange(1, 20)
second_number = random.randrange(1, 10)

while True:
    answear = input(f'Please enter the result of multiplying two numbers {first_number} * {second_number} = ')
    
    if answear.isdigit():
        if int(answear) == int(first_number) * int(second_number):
            print('CONGRATULATIONS!!! You are right and win!')
            break
        else:
            print(f'Sorry, you are wrong. The right answear is {int(first_number) * int(second_number)}.')
            break
    else:
        print('Please, enter your answear with digets.')

