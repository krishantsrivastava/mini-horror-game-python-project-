print("welcome to mini horror game made in python")

choice = input("Enter yes to start or no to exit: ")

if choice == "no":
    print("you are noob")

else:
    print("welcome to mini horror game")

    choice2 = input("You have two options: find exit or give up: ")

    if choice2 == "find exit":
        print("congratulations you escaped")

    else:
        print("you died")