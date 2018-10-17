import random
import string

list_numbers = [(random.randint(1, 25)) for i in range(10)]

alphabet = []
for letter in string.ascii_lowercase:
    alphabet.append(letter)

sorted_list_number = sorted(list_numbers, reverse=True)

print('List number: ', list_numbers, '\n',
      'Sorted list number: ', sorted_list_number)

letter_from_alpha = []
for j in sorted_list_number:
    letter_from_alpha.append(alphabet[j])

result = dict(zip(sorted_list_number, letter_from_alpha))
print('Dictionary: ', result)
