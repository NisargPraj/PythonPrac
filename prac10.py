#prac 10
import random

flag = 1

# random = random.randrange(1, 10, 1)
# print(type(random))

while flag == 1:
    r = random.randrange(1, 10, 1)
    user = input("Guess the number between 1 and 9: ")

    if user == 'exit':
        flag = 0
    elif r == int(user):
        print("Your guess is Exactly Right")
    elif r > int(user):
        print("Your guess is Too Low")
    elif r < int(user):
        print("Your guess is Too High")
