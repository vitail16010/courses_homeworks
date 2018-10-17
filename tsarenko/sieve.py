user_input = int(input("Enter number:"))

old_list = list(range(user_input))

old_list[1] = 0

prime_index = 2
while prime_index < user_input:
    if old_list[prime_index] != 0:
        composite_index = prime_index * 2
        while composite_index < user_input:
            old_list[composite_index] = 0
            composite_index = composite_index + prime_index
    prime_index += 1

new_list = [i for i in old_list if i != 0]

print(new_list)

