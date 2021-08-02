"GettingStartedWithPython"
#This file contain the basics of Python.
#The following part will introduce you a way to print something on screen
my_container = "Hello Soroush"
print(my_container)
#The following part will show
prize = 6.99
print(type(prize))

number = 54
print(type(number))

first: float = 8.5
second: int = 6
total = first * -second
print(total)

my_string = "Tama"+""+"ran"
print(my_string)

name1 = "StarFire"
sentence = "Hi There, " + name1
print(sentence)

if 6 < 9:
    print(True)
if 6 > 9:
    print(True)
name2 = "Mario"
if name2 == "Donald":
    print("Hi Donald!")
if name2 != "Donald":
    print("You're not Donald")

a = False
if a:
    print("a is true")
if a==False:
    print("a is false")

b = True
if b:
    print("b is true")
if b==False:
    print("b is false")

c = False
if c:
    print("c is true")
else:
    print("c is false")

name="BlackCanary"
if name=="SuperGirl":
    print("Hi SuperGirl!")
elif name=="StarFire":
    print("Hi StarFire!")
else:
    print("You're not StarFire or SuperGirl!")

name="StarFire"
if name=="SuperGirl":
    print("Hi SuperGirl!")
elif name=="StarFire":
    print("Hi StarFire!")
else:
    print("You're not StarFire or SuperGirl!")

import time

count = 1

while count <= 10:
    print(str(count) + " WonderWoman")
    count += 1
    time.sleep(0.9)

import time

count = 1

while count <= 10:
    print(str(count) + " WonderWoman")
    count += 1
    time.sleep(0.5)

print("Ready or not here I come!")

attempts = 0
correct_pin = "1221"

while attempts < 3:
    entered_pin = input("Enter PIN: ")
    if entered_pin == correct_pin:
        print("You've successfully logged in!")
        break
    else:
        print("Incorrect! Try again...")
        attempts += 1
if attempts >= 3:
    print("Oops!you are haghighatan ver gav!")
