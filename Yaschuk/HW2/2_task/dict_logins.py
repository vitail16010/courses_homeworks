import random

passw = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999']
log = {
    '1':  [passw[0], random.randint(1, 10)],
    'Petrovnyi': [passw[1], random.randint(1, 10)],
    'Ikorniy': [passw[2], random.randint(1, 10)],
    'Resultativniy': [passw[3], random.randint(1, 10)],
    'Filipov': [passw[4], random.randint(1, 10)],
    'Morkovniy': [passw[5], random.randint(1, 10)],
    'Delovoy': [passw[6], random.randint(1, 10)],
    'Ptenec': [passw[7], random.randint(1, 10)],
    'Holodec': [passw[8], random.randint(1, 10)],
    'Severniy': [passw[9], random.randint(1, 10)]
}
x = input('login: ')
if x in log:
    print(log[x][1])
else :
    y = input('Greate your password: ')
    log.setdefault(x)
    passw.append(y)
    log[x] = f'{passw[-1]} {random.randint(1, 10)}'
    print(log)
