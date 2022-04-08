#rock paper scissor prac 9
flag = 1

while flag == 1:

    a = input("Player One choose(Rock(R)/Paper(P)/Scissor(S)): ").lower()
    b = input("Player Two choose(Rock(R)/Paper(P)/Scissor(S)): ").lower()

    if a == 'r' and b == 'r':
        print("Draw!")
    elif a == 'r' and b == 'p':
        print("Player Two Wins!")
    elif a == 'r' and b == 's':
        print("Player One Wins!")
    elif a == 'p' and b == 'r':
        print("Player One Wins!")
    elif a == 'p' and b == 'p':
        print("Draw!")
    elif a == 'p' and b == 's':
        print("Player Two Wins!")
    elif a == 's' and b == 'r':
        print("Player Two Wins!")
    elif a == 's' and b == 'p':
        print("Player One Wins!")
    elif a == 's' and b == 's':
        print("Draw")
    else:
        print("Enter Valid option")

    choice = input("Do you wish to continue? y/n: ").lower()

    if choice == 'y':
        flag = 1
    elif choice == 'n':
        flag = 0
    else:
        print("choose correct option")