#The valid phone number program.

#Make a program that checks if a string is in the right format for a phone number. 
#The program should check that the string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.

while True:
    given_phone = input('Please, enter your telephone number: ')

    if given_phone.isdigit():
        if len(given_phone)==10:
            print(f'Your telephone number {given_phone} varified.')
            break
        else:
            print(f"Your telephone number {given_phone} doesn’t have 10 digits.")
    else:
        print('Wrong format. Use just 10 digets.')