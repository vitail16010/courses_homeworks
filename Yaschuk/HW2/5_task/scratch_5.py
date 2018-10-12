import random
from string import ascii_letters as a_l
numb = []
a_l = list(a_l)
for i in range(len(a_l)):
    numb.append(random.randint(0, 51))
numb.sort()
numb.reverse()
for x in range(len(a_l)):
    numb[x] = str(numb[x]) + a_l[(numb[x])] + (''.join(random.choice(a_l) for n in range(10)))

print(numb)
