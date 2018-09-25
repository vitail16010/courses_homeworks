import random

number = int(input("Please enter a number:"))

random_number = random.randint(0, number)

print("The random number from 0 to", number, "is", random_number)

print("Here are", random_number, "numbers from range 0 to", number, ":",
      random.sample(range(number), random_number))
