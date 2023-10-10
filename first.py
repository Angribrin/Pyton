import random

user_name = input("What is youre name?\n")

number = random.randint(1,20)
counter = 0

while True:
    guess_number = int(input("Enter youre number: "))
    if guess_number == number :
        print("you are the winner")
        break
    elif 1<=guess_number<=20 and guess_number<number:
        print("Youre number is bigger")
    elif 1<=guess_number<=20 and guess_number>number:
        print("Youre number is less")
    elif not 1<=guess_number<=20:
        print("Yore number is not in the range")
