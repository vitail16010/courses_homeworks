import random
random_number = random.randint(1000, 1000000)
print("Random number = ", random_number)
print("#4 element = ", ((random_number % 10000)-(random_number % 1000))//1000)
