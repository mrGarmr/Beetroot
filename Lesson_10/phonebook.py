import os, json, time

DATA_FILE = os.path.dirname(__file__)+'/phonebook.pnb'
CACHE_ADDRESSBOOK = {}


def cache():
    global CACHE_ADDRESSBOOK
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as data:
            CACHE_ADDRESSBOOK = json.load(data)

    else:
        with open(DATA_FILE,'a') as data:
            json.dump(CACHE_ADDRESSBOOK, data)
        

def create_contact():
    print(f"{'New contact':^60}")
    while True:
        first_name = input('Please, enter First name: ')
        last_name = input('Please, enter Last name: ')
        phone_number = input('Please, enter Phone number: ')
        address = input('Please, enter address: ')
        if (first_name, last_name, phone_number, address):
            id = str(time.time()).split('.')[1]
            phonebook = {id : {'first_name' : first_name, 'last_name' : last_name, 'phone_number' : phone_number, 'address' : address}}
            save(phonebook)
            print(60*'_')
            break
        else:
            print('Your input was wrong, please try again.')
            
def edit_contact():
    print(60*'_')
    print(f"|{'We are going to edit contact. First we need the proper contact?': <60}|")
    print(f"|{'1. Type "name"                    to find contact by First name.': <60}|")
    print(f"|{'2. Type "surname" or "last name"  to delete contact by  Last name.': <60}|")
    print(f"|{'3. Type "phone"                   to delete contact by Phone number.': <60}|")
    print(60*'_')

    decision = input().lower()
    decision = decision.lower()

    if decision == '1' or decision == 'name' or decision == 'тфьу':
        return update_contact(find_by_name())
    elif decision == '2' or decision == 'surname' or decision == 'last name' or decision == 'lastname' or decision == 'дфіе тфьу' or decision == 'дфіетфьу':
        return update_contact(find_by_last_name())
    elif decision == '3' or decision == 'phone' or decision == 'зрщту' or decision == 'номер':
        return update_contact(find_by_phone())


def find_all():
    return show_phonebook(CACHE_ADDRESSBOOK)

def find():
    print(60*'_')
    print(f"|{'In what fields you want to look in?': <60}|")
    print(f"|{'1. Type "name"                    to find in First name.': <60}|")
    print(f"|{'2. Type "surname" or "last name"  to find in Last name.': <60}|")
    print(f"|{'3. Type "phone"                   to find in Phone number.': <60}|")
    print(f"|{'4. Type "address"                 to find in Address.': <60}|")
    print(60*'_')

    decision = input().lower()
    decision = decision.lower()

    if decision == '1' or decision == 'name' or decision == 'тфьу':
        return show_phonebook(find_by_name())
    elif decision == '2' or decision == 'surname' or decision == 'last name' or decision == 'lastname' or decision == 'дфіе тфьу' or decision == 'дфіетфьу':
        return show_phonebook(find_by_last_name())
    elif decision == '3' or decision == 'phone' or decision == 'зрщту' or decision == 'номер':
        return show_phonebook(find_by_phone())
    elif decision == '4' or decision == 'address' or decision == 'adress' or decision == 'adres' or decision == 'адрес' or decision == 'фввкуіі':
        return show_phonebook(find_by_address())

def find_by_name():
    print(60*'_')
    print(f"|{'Type name you want to find in First names.': <60}|")
    print(60*'-')
    name = input().lower()
    result=[]
    for item in CACHE_ADDRESSBOOK:
        if name in CACHE_ADDRESSBOOK[item]['first_name'].lower():
            result.append(item)
    print(60*'-')
    return result

def find_by_last_name():
    print(60*'_')
    print(f"|{'Type last name you want to find in Last names.': <60}|")
    surname = input().lower()
    result=[]
    for item in CACHE_ADDRESSBOOK:
        if surname in CACHE_ADDRESSBOOK[item]['last_name'].lower():
            result.append(item)
    print(60*'-')
    return result
    
def find_by_phone():
    print(60*'_')
    print(f"|{'Type phone you want to find in Phones.': <60}|")
    phone = input().lower()
    result=[]
    for item in CACHE_ADDRESSBOOK:
        if phone in CACHE_ADDRESSBOOK[item]['phone'].lower():
            result.append(item)
    print(60*'-')
    return result

def find_by_address():
    print(60*'_')
    print(f"|{'Type adress you want to find in Address.': <60}|")
    address = input().lower()
    result=[]
    for item in CACHE_ADDRESSBOOK:
        if address in CACHE_ADDRESSBOOK[item]['address'].lower():
            result.append(item)
    print(60*'-')
    return result

def input_error():
    pass
 
def update_contact(contact):
    delete_contact(contact)
    create_contact()
    
def delete_contact_show():
    print(60*'_')
    print(f"|{'We are going to delete contact. In what field to look in?': <60}|")
    print(f"|{'1. Type "name"                    to delete contact by First name.': <60}|")
    print(f"|{'2. Type "surname" or "last name"  to delete contact by  Last name.': <60}|")
    print(f"|{'3. Type "phone"                   to delete contact by Phone number.': <60}|")
    print(60*'_')

    decision = input().lower()
    decision = decision.lower()

    if decision == '1' or decision == 'name' or decision == 'тфьу':
        return delete_contact(find_by_name())
    elif decision == '2' or decision == 'surname' or decision == 'last name' or decision == 'lastname' or decision == 'дфіе тфьу' or decision == 'дфіетфьу':
        return delete_contact(find_by_last_name())
    elif decision == '3' or decision == 'phone' or decision == 'зрщту' or decision == 'номер':
        return delete_contact(find_by_phone())

def delete_contact(contact):
    global CACHE_ADDRESSBOOK
    show_phonebook(contact)
    if len(contact)>1:
        print('We find more than one contact. Please enter the exact id to edit|delete:')
        del CACHE_ADDRESSBOOK[input('id: ')]
        save(CACHE_ADDRESSBOOK)

    elif contact[0]:
        print(f"|{'We are going to delete contact.': ^60}|")
        print(f'{CACHE_ADDRESSBOOK[contact[0]]["first_name"]} {CACHE_ADDRESSBOOK[contact[0]]["last_name"]}')
        print(f"|{'ARE YOU SURE? Yes or No.': ^60}|")
        if y_n_decision():
            del CACHE_ADDRESSBOOK[contact[0]]
            save(CACHE_ADDRESSBOOK)
    else:
        print(f"|{'Nothing to delete.': ^60}|")

def save(phonebook):
    if phonebook != CACHE_ADDRESSBOOK:
        CACHE_ADDRESSBOOK.update(phonebook)
        with open(DATA_FILE, "w") as my_file:
            json.dump(CACHE_ADDRESSBOOK, my_file)
    else:
        with open(DATA_FILE, "w") as my_file:
            json.dump(CACHE_ADDRESSBOOK, my_file)

    print(63*'_')    
    print(f"|{' Successfully saved.': ^63}|")
    print(63*'_')

def exit():
    return 'exit'

def handler(user_input):

    if user_input in ANSWEARS.keys():
        return ANSWEARS[user_input]()
    
    elif user_input in ADD:
        print('Maybe you mean "add" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        if y_n_decision():
            return create_contact()
        
    elif user_input in CHANGE:
        print('Maybe you mean "change" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        if y_n_decision():
            return edit_contact()

    elif user_input in FIND:
        print('Maybe you mean "find" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        if y_n_decision():
            return find()

    elif user_input in HELP:
        print('Maybe you mean "help" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        if y_n_decision():
            return print_functionality()

    elif user_input in DELETE:
        print('Maybe you mean "delete" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        if y_n_decision():
            return delete_contact_show()

    elif user_input in SHOW:
        print('Maybe you mean "show" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return show_phonebook()
    else:
        return input_error()

def show_phonebook(data):
    print(100*'_')
    print(f"|{'I have found the following:': ^96}|")
    print(100*'_')
    print('|   ID   |     Last  name     |     First name     | Phone number  |          Address            |')
    print(100*'-')
    for item in data:
        print(f'|{item:^8}|{CACHE_ADDRESSBOOK[item]['last_name']:^20}|{CACHE_ADDRESSBOOK[item]['first_name']:^20}|{CACHE_ADDRESSBOOK[item]['phone_number']:^15}|{CACHE_ADDRESSBOOK[item]['address']:^29}|' )
        print(100*'-')

def print_functionality():
    print(65 * '_')
    print('| 1. Type "add"    to add new contact.                           |\n'
            '| 2. Type "find"   to see information that you are looking for.  |\n'
            '| 3. Type "delete" to delete information that you don\'t need.    |\n' 
            '| 4. Type "show"   to show you all phonebook.                    |\n'
            '| 5. Type "edit"   to edit your contact.                         |\n'
            '| 6. Type "save"   to save and exit.                             |\n'
            '| 0. Type "exit"   to exit.                                      |')
    print(65 * '_')

def y_n_decision():
    decision = str(input())
    decision = decision.lower()
    if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
        return True
    else:
        return False
    
    
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    print_functionality()
    cache()
    
    while True:
        print(f"|{' What do you want to do?': ^64}|")
        print(f"|{' Type exact command you want to do.': ^64}|")
        print(f"|{' "help" for list of commands.': ^64}|")
        print(f"|{' "exit" to exit.': ^64}|")
        print(65*'_', '\n')
        
        user_input = input().lower()
        output = handler(user_input)

        if user_input == 'exit' or output == 'exit':
            break
        
ANSWEARS = {
    '1': create_contact,'add': create_contact, 'ad': create_contact, '+': create_contact, 'фвв': create_contact, 'добавити': create_contact,
    '2': find, 'find': find, 'аштв': find, 'пошук': find, 'знайти': find,
    '3': delete_contact_show, 'delete': delete_contact_show, 'видалити': delete_contact_show,
    '4': find_all, 'show': find_all, 'ырщц': find_all, 'показати': find_all, 'телефонна книга': find_all, 'книга': find_all, 'book': find_all,
    '5': edit_contact, 'change': edit_contact, 'update': edit_contact, 'змінити': edit_contact, 'edit': edit_contact, 
    '6': print_functionality,'help': print_functionality, 'допомога': print_functionality, 
    '0': exit, 'close': exit, 'exit': exit, 'учше': exit, 'вихід': exit, 'вийти': exit,
    }

ADD = ['a', 'ad', 'addd', 'asd', 'asdd', 'sdd', 'adf', 'фів', 'івв', 'фівв', 'фввв', 'фва', 'вв', 'ыва', 'фвы', 'фыв',
       'явв', 'фв',]

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
