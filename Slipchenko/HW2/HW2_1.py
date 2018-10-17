import random
import string

list_letters = []
for i in range(10):
    a = []
    for n in range(random.randint(1, 9)):
        a.append(''.join(random.choice(string.ascii_letters)))
    list_letters.append(''.join(a))

print('List random letter: ', list_letters)

list_numbers = []
for h in range(10):
    b = []
    for j in range(random.randint(1, 9)):
        b.append(''.join(random.choice(string.digits)))
    list_numbers.append(''.join(b))

print('List random numbers: ', list_numbers)

dict_lists = dict(zip(list_letters, list_numbers))
print('Dictionary: ', dict_lists)
