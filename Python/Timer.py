import time

def countdown(clock):

    while clock:
        mins, secs = divmod(clock, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        clock -= 1

    print("It's Over!")

t = input("Enter the time in seconds: ")
countdown(int(t))