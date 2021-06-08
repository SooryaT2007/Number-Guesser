import time
import random

def verify_no(number):
    try:
        number = int(number)
        return True
    except:
        return False


usr_name = input("Welcome! Please enter your name : ")
first = input("> Enter your minimum number : ")
last = input("> Enter your maximum number : ")
if verify_no(first)==True:
    first = int(first)
    if verify_no(last)==True:
        last = int(last)
        rand_num= random.randint(first,last)
        while True:
            num = input("Enter your guess : ")
            if verify_no(num)==True:
                num = int(num)
                if num > rand_num:
                    print("Your number is greater than the random number.")
                elif num < rand_num:
                    print("Your number is smaller than the random number.")
                elif num==rand_num:
                    print("You are a Genius.")
                    print(f"Thank you {usr_name}.")
                    break
            else:
                print("Please enter a valid number.")
    else:
        print(f"Maximum number {last} is invalid.")
else:
    print(f"Minmum number {first} is not valid.")

time.sleep(10)