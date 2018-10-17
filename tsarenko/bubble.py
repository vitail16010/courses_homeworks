import random

random_length = random.randint(1, 20)

my_list = random.sample(range(100), random_length)
print(my_list)

n = 1

while n < len(my_list):
    for a in range(len(my_list) - n):
        if my_list[a] > my_list[a + 1]:
            my_list[a], my_list[a+1] = my_list[a+1], my_list[a]
    n += 1
print(my_list)
