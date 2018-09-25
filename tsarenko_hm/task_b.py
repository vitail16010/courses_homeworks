import random

random_number = random.randint(1000, 1000000)

result_4sign = ((random_number % 10000) - (random_number % 1000)) // 1000

print("The random number is", random_number, "its 4th sign is", result_4sign)
