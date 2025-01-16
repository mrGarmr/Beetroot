import os, json, time

DATA_FILE = 'phonebook.pnb'

def validation(first_name, last_name, phone_number, address):
     

    return True

def create_contact():
    print('Adding')
    while True:
        first_name = input('Please, enter First name: ')
        last_name = input('Please, enter Last name: ')
        phone_number = input('Please, enter Phone number: ')
        address = input('Please, enter address: ')
        if (first_name, last_name, phone_number, address):
            id = str(time.time()).split('.')[1]
            phonebook = {id : {'first_name' : first_name, 'last_name' : last_name, 'phone_number' : phone_number, 'address' : address}}
            save(phonebook)
            break
        else:
            print('Your input was wrong, please try again.')
        
    # first_name, last_name, phone_number, country
    

def edit_contact():
    pass

def find_all():
    with open(DATA_FILE,'r') as data:
        phonebook = json.load(data)
    return phonebook

def input_error():
    pass
def update_contact():
    pass
def delete_contact():
    pass

def save(phonebook):
    print(phonebook)
    with open(DATA_FILE,'w+') as data:
        json.dump(phonebook,data)



def exit():
    return 'exit'

def handler(user_input):

    if user_input in ANSWEARS.keys():
        return ANSWEARS[user_input]()
    
    elif user_input in ADD:
        print('Maybe you mean "add" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return create_contact()
        
    elif user_input in CHANGE:
        print('Maybe you mean "change" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return edit_contact()

    elif user_input in FIND:
        print('Maybe you mean "find" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return show_phonebook()

    elif user_input in HELP:
        print('Maybe you mean "help" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return print_functionality()

    elif user_input in DELETE:
        print('Maybe you mean "delete" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return delete_contact()

    elif user_input in SHOW:
        print('Maybe you mean "show" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return show_phonebook()
    else:
        return input_error()

def show_phonebook():
    
    print("I've found the following:")

        # шапка

    print(100*'_')
    print('|   ID   |     Last  name     |     First name     | Phone number  |          Address            |')
    print(100*'-')
    data = find_all()
    for item in data:
        print(f'|{item:^8}|{data[item]['last_name']:^20}|{data[item]['first_name']:^20}|{data[item]['phone_number']:^15}|{data[item]['address']:^29}|' )
        print(100*'-')
        
       
    
def print_functionality():
    print(65 * '_')
    print('| 1. Type "add"    to add new contact.                           |\n'
            '| 2. Type "find"   to see information that you are looking for.  |\n'
            '| 3. Type "delete" to delete information that you don\'t need.    |\n' 
            '| 4. Type "show"   to show you all phonebook.                    |\n'
            '| 5. Type "save"   to save and exit.                             |\n'
            '| 0. Type "exit"   to exit.                                      |')
    print(65 * '_')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_functionality()
    while True:
        print()
        user_input = input(
            '\n|   What do you want to do?                                      |\n'
            '|   Type exact command you want to do,                           |\n'
            '|   "help" for list of commands.                                 |\n'
            '|   "exit" to exit.                                              |\n'
            '_________________________________________________________________\n'
                )
        
        
        

        user_input = user_input.lower()
        output = handler(user_input)

        if user_input == 'exit' or output == 'exit':
            break
        
ANSWEARS = {'add': create_contact, 'ad': create_contact, '+': create_contact, 'фвв': create_contact, '1': create_contact,
'change': update_contact, 'delete': delete_contact, '-': delete_contact, '3': delete_contact, 'help': print_functionality,
            'close': exit, 'exit': exit, 'учше': exit,
            'find': show_phonebook, 'аштв': show_phonebook, 'show': show_phonebook, 'ырщц': show_phonebook, '2': show_phonebook}

ADD = ['a', 'ad', 'addd', 'asd', 'asdd', 'sdd', 'adf', 'фів', 'івв', 'фівв', 'фввв', 'фва', 'вв', 'ыва', 'фвы', 'фыв',
       'явв', 'фв']

CHANGE = ['chane', 'chnge', 'cange', 'chenge', 'hange', 'chng', 'cchenge', 'chhenge', 'cheenge', 'chaange', 'сменить',
          'chang', 'срутпу', 'срутп', 'менять', 'изменить', 'срфтп', 'рсфтпу', 'срутпу', 'cheng']

DELETE = ['вуд', '-', 'del', 'вудуеу', 'вуфдуеу', 'dealete', 'elete', 'elet', 'delet', 'dlte', 'dlt', 'lete', 'dealete',
          'вудуе', 'удалить', 'pop']

FIND = ['fnd', 'ind', 'fid', 'fin', 'faind', 'fand', 'ffind', 'fiind', 'finnd', 'findd', 'seek', 'look', 'look for',
        'атв', 'афтв', 'штв', 'афт', 'поиск', 'искать', 'найти', 'шштв']

HELP = ['&', '?', 'hlp', 'what', 'why', 'where', 'how', 'elp', 'hep', 'hel', 'healp', 'halp', 'hhelp', 'heelp', 'hellp',
        'helpp', 'рфдз', 'рдз', 'руз', 'руд', 'помощь']
        
SHOW = ['ырща', 'ырщцу', 'showe', 'schow', 'schove', 'chov', 'shove', 'schov', 'schowe', 'how', 'sho', 'shouv', 'шов',
        'ірщцу', 'показать', 'рщц', 'ірщм']

if __name__ == '__main__':
    main()
