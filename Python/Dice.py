import random
while True:
    start = input('Do you want to start?(Y/N)').upper()
    if start == 'Y':
        a = random.randint(1,6)
        print(a)

    else:
        print('Program Closed !')
        break