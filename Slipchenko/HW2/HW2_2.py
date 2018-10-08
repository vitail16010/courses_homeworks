import random
import string

random_number = random.choice(string.digits)

login_and_pass = {
    'Wiwhite': 'Splash@{}'.format(random_number),
    'Killer': 'Kill@{}'.format(random_number),
    'piG': 'Xry@{}'.format(random_number),
    'Alex': 'Name@{}'.format(random_number),
    'Blacky': 'black@{}'.format(random_number),
    'Nano': 'nan0@{}'.format(random_number),
    'MyName': 'NAME@{}'.format(random_number),
    'greatGetsby': 'GG@{}'.format(random_number),
    'Monkey': 'babanas@{}'.format(random_number),
    'littlebig': 'faradenza@{}'.format(random_number)
}

print('Dictionary: ', login_and_pass)

login = input('Enter your login: ')

if login in login_and_pass:
    print(random_number)
else:
    login_and_pass[login] = login + random_number
    print('Dictionary: ', login_and_pass)
