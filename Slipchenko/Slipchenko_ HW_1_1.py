import random

number_of_user = int(input("Enter the number:"))

random_number_user = random.randint(0, number_of_user)
print("Random number:", random_number_user)

generate_sample_random_number = \
    random.sample(range(number_of_user), random_number_user)
print("Random sampling:", generate_sample_random_number)