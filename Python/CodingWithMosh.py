#formatted strings
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder '
msg = f'{first} [{last}] is a coder'
print(msg)
#String Methods
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('o'))
print(course.replace('Beginners','Absolute Beginners'))
print(course.replace('P','J'))
print('Python' in course)
#Arithmetic Operations
x = 10
x = x + 3
x += 3 #This is shorted form of upper line
print(x)
#Operator Precedence
y = 10 + 3 * 2
print(y)
#Math Functions
import math
from typing import List

print(math.floor(2.9))
z = 2.9
print(round(z))
print(abs(-2.9))
#if statements
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear Warm Cloth")
else:
    print("It's a lovely day")

print("Enjoy your day")
#Practice Of The Last One
import math
price = int(input("How Much You Gonna Spend?"))
buyer = input("True/False")
if buyer:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Down Payment: ${down_payment}")
#Logical Operator
has_high_income = input("True/False")
has_high_credit = input("True/False")

if has_high_income and not has_high_credit:
    print("Good To Go!")
#Comparison Operators
temp = input("What is the temperature today? ")
converted_temp = int(temp)

if converted_temp > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

#Practice The Last Part
name = input("What is your name? ")

if len(name) < 3:
    print("Not Long Enough!")

elif len(name) > 50:
    print("Tooo Long!")

else:
    print("Long Enough!")

#Weight Converter
Weight = int(input("Enter Your Weight: "))
Kind = input("Kilograms/Pounds")

if Kind == "Kilograms":
    YourWeight = Weight*2.205
elif Kind == "Pounds":
    YourWeight = Weight/2.205
print(f"Your Weight is : {YourWeight}")

#While Loops
Guess_count = 1
while Guess_count <= 5:
    print('*' * Guess_count)
    Guess_count = Guess_count + 1
print("Done")

#Gussing Game
secret_number = 9
Guess_count = 0
Guess_limit = 3
while Guess_count < Guess_limit:
    guess = int(input('Guess: '))
    Guess_count += 1
    if guess == secret_number:
        print('You Won!')
        break
else:
    print("Sorry!")

#Car Game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
                """)
    elif command == "quit":
        break
    else:
        print("Sorry.I don't understand that!")

#For Loops
prices = range(10, 31, 10)

total = 0
for price in prices:
    total += price
print(f"Total: {total}")

#Nested Loops
for x in range(4):
    for y in range(3):
       print(f'({x}, {y})')

#Challenge(Hard)

Numbers = [5, 2, 5, 2, 2]

for x_count in Numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
                    
#Another Version Of The Last Challenge
numberss = [5, 2, 5, 2, 2]
for x_count in numberss:
    print('x' * x_count)

#Lists
names = ['Soroush', 'Fatemeh', 'Fitness', 'Technology', 'Computer']
names[0] = 'Soroosh'
print(names[0:2])

#Challenges

numbers = [512, 1024, 256, 768]
usersnumber = int(input("How much do want?"))
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
    elif usersnumber > max:
        max = usersnumber
print(max)

#2D List

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]

]
for row in matrix:
    for item in row:
        print(item)

#Additional part for the upper one

matrix[0][1] = 20
#With this part you can change a specific part of Matrix

#List Methods
numbers = [5, 3, 2, 6, 7]
numbers.remove()
numbers.index()
numbers.append()
numbers.pop()
numbers.remove()
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
print(numbers.count())
print(numbers.index(6))
#Instead of index for finding a variable you can use the "IN" operator
print(6 in numbers)

#Challenge
Duplicates = [1, 1, 2, 2, 3, 3 ,4 ,4]
uniques = []
for number in Duplicates:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#Tuples
Cardinal = (1, 2, 3)
print(Cardinal[0])

#Unpacking
coordinates = (1, 2, 4)
a, b, c = coordinates
print(a)
#You can also use the Unpacking method for Lists

#Dictionaries

GirlFriendOfMine = {
    "name":"Fatemeh",
    "age": 16,
    "is_thebest": True
}
GirlFriendOfMine["name"] = "FatemehGhorbanTalemi" #You can update a value in a dictionary with this line.
print(GirlFriendOfMine.get("name")) #Instead of this line I can use this one:print(GirlFriendOfMine["name"]).
print(GirlFriendOfMine.get("birthdate", "Nov 8 2005")) #With this line of code you can access the values of dictionary.

#Challenge

phone = input("Phone: ")
digits_mapping = {
     "1": "One",
     "2": "Two",
     "3": "Three",
     "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

#Emojis

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😃",
    ":(": "😞"
}
output = " "
for word in words:
    output += emojis.get(word, word) + " "
print(output)

#Functions
#"def" is short form of definition which when we type it in Python interpreter, the interpreter will know that we want to use a function.
#Always use a meaningful name for functions
#When we use a function we should add two blank lines after them.


def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')
print("Start")
greet_user("Fatemeh", "Talemi") #These are positinal arguments
print("Finish")


#Keyword Arguments
#These arguments will improve the readability of our code.
#Keyword arguments should come after positional arguments

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')
print("Start")
greet_user(last_name="Fatemeh", first_name="Talemi")
print("Finish")

#Return Statement
#By default every functions in Python will return none, so for preventing that in our code we should use return statement in our function

def square(number):
    return number * number

print(square(3))

#Reusable Function

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
     ":)": "😃",
     ":(": "😞"
    }
    output = ""
    for word in words:
       output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))

#Expections

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')

#Classes

class Point:
    def move(self):
        print("move")
    
    def draw(self):
        print("Soroush")

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

#Constractors

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

point = Point(10, 20)
print(point.x)

#Challenge

class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()

#Inheritance
#This function will give us the ability to summeries the class that we want to repeat in our code lines to prevent repetitive classes.

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

dog1 = Dog()
dog1.bark()

#Modules
#Modules help us to organize our codes with import functions.

import Converters
from Converters import kg_to_lbs
kg_to_lbs(100)

print(Converters.kg_to_lbs(70))

#Challenge
from thebest import find_max
numbers = [512, 1024, 256, 768]
max = find_max(numbers)
print(max)

#Packages
import Ecommerce.shipping
Ecommerce.shipping.calc_shipping()
 #or
from Ecommerce.shipping import calc_shipping
calc_shipping() 

#Generating Random Values
import random
 
members = ['Soroush', 'Ramshar', 'Pourya', 'Abbas']
leader = random.choice(members)
print(leader)

#Challenge
import random
class Dice:
    def roll(self):
        third = random.randint(1, 12)
        return third

dice = Dice()
print(dice.roll())

#Files&Directories

from pathlib import Path
#Absolute path
#Relative path
path = Path("Ecommerce")
print(path.exists())
#Another function of Pathlib
from pathlib import Path
path = Path("Emails")
print(path.mkdir())
#Another One
from pathlib import Path
path = Path("Emails")
print(path.rmdir())
#Another One
from pathlib import Path
path = Path()
for file in path.glob('*.py'):
    print(file)

#PyPi&PiP
#pip install openpyxl
#The core concept of Python will close here.See you in the next tutorial.