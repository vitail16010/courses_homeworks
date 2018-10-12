from string import ascii_letters as a_l
import random

letters_list = []
number_list = []
dict_ln = {}

for i in range(10):
    a = []
    for x in range(random.randint(1, 10)):
        a.append(random.choice(a_l))
    letters_list.append(''.join(a))

for n in range(10):
    number_list.append(random.randint(1, 10))

for y in range(10):
    dict_ln.update({letters_list[y]: number_list[y]})

print(dict_ln)