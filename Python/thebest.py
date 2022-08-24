def find_max(numbers):
    numbers = [512, 1024, 256, 768]
    usersnumber = int(input("How much do want?"))
    max = numbers[0]
    for number in numbers:
     if number > max:
        max = number
     elif usersnumber > max:
        max = usersnumber
        return max