#Calculating factorial in Python

import math
the_number = int(input("What is your desired number : "))
print(math.factorial(the_number))

#Price of the house

house_price = int(input("What is the price of the house: "))
credit = True
if credit:
    print("They need to put down 10%")
    print(f"{house_price*0.1} is the amount you should get!")
else:
    print("They need to put down 20%")
    print(f"{house_price*0.2} is the amount you should get!")


#Logical Operators & Comparison Operators

name = input("Your name: ")
name_length = len(name)

if name_length <= 3:
    print("Name must be more than 3 characters!")
elif name_length >= 50:
    print("Name must be shorter than 50 characters!")
else:
    print("You are good to go!")

#While Loops

number = 0
while number <= 6:
    print("Yes!")
    number += 1

#Car Game Version 1.0

command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car Started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
        start - to start the game
        stop - to stop the game
        quit - to quit the game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry for that!")


#For loops

for item in 'Python':
    print(item)

for item in range(0,10,2):
    print(item)

#Nested For Loops

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5,2,5,2,2]
for item in numbers:
    print("X" * item)

#Finding the best

numbers = [100, 200, 400, 20, 90]
max = numbers [0]
for number in numbers:
    if number > max:
        max = number
print(max)

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
for row in matrix:
    for item in row:
        print(item)


#List methods
numbers = [4,32,24,56,10]
numbers.append(20)
numbers.insert(2, 50)
numbers.remove(24)
numbers.pop()
numbers.clear()
numbers2 = numbers.copy()
print(numbers)
print(numbers.index(56))
print(24 in numbers)

#Deleting duplicates
numbers = [3,3,4,4,4,1,2,3,90]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#Unpacking

numbers = [1,2,3]
x,y,z = numbers
print(y)

#Functions

def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome aboard')


print("Start")
greet_user("Soroush")
print("Finish")

#keyword arguments
#If your code contains numerical arguments you should use keyword arguments to improve its readability
#But if it's a string you should use positional arguments
#Positional is before keyword arguments
def great_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

print("Start")
great_user(last_name="Soroush",first_name="MasoomBabaei")
print("Finish")


#Exceptions
try:
    age = int(input("Age: "))
    income = int(input("Income: "))
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')

#Classes

class Point