import random

random_number = random.randint(1000, 1000000)
print("Random number between 1000 and 1000000 is:", random_number)

fourth_sign_random_number = \
    ((random_number % 10000)-(random_number % 1000))//1000
print("4th sign is:", fourth_sign_random_number)