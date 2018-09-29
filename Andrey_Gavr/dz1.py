import random

user_number = int(input("введите целое число от 1 до 10:"))
if user_number <= 0 or user_number > 10:
    print("Ошибка, повторите ввод числа")
else:
    print(user_number)
    random_choice = random.randint(0, user_number)
    print(random_choice)
    sequence = random.sample(range(0, user_number), random_choice)
    print(sequence)
