import random

def start_game():
    print("Welcome to the Simple Quest Game!")
    print("You find yourself in a mysterious forest. There are two paths ahead.")
    print("1. Go left")
    print("2. Go right")

    choice = input("Choose a path (1/2): ")

    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        start_game()

def left_path():
    print("You go left and encounter a wild creature.")
    print("1. Try to run away")
    print("2. Attempt to befriend the creature")

    choice = input("Choose an action (1/2): ")

    if choice == "1":
        if random.randint(0, 1) == 0:
            print("You successfully escape from the creature. Your journey continues.")
            continue_journey()
        else:
            print("You couldn't run away and were eaten. Game over.")
    elif choice == "2":
        print("Your attempt to befriend the creature succeeds! You now have a loyal companion.")
        continue_journey()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        left_path()

def right_path():
    print("You go right and discover a hidden treasure!")
    print("Congratulations! You win the game.")

def continue_journey():
    print("You continue your journey and come across two bridges.")
    print("1. Cross the wooden bridge")
    print("2. Cross the stone bridge")

    choice = input("Choose a bridge (1/2): ")

    if choice == "1":
        print("The wooden bridge is unstable, and you fall into the river. Game over.")
    elif choice == "2":
        print("You successfully cross the stone bridge and continue your adventure.")
        right_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        continue_journey()

if __name__ == "__main__":
    start_game()