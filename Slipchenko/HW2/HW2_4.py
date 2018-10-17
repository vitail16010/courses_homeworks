input_user = int(input('Enter number: '))

for i in range(input_user):
    print(' ' * (input_user-i) + ('* ' * (i+1)))
