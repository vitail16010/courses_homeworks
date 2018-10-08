import random
user_random = int(input("Num:"))
random_number = int(1)
if user_random < 0:
    print("Num<0")
else:
    random_number = random.randint(0, user_random)
random_range = random.sample(range(0, user_random), random_number)
print("Random number = ", random_number, "\nRandom range = ", random_range)
