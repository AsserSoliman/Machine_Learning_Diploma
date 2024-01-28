import random

user_trials = 0
max_trials = 0
limit = 0

def Greeting():
    print("\n\t ****** Welcome To Guessing Game *******\n\n")

def show_game_levels():
    print("Game Levels:\n------------\n")
    
    print("1) Easy")
    print("\t Limit:[1-10]")
    print("\t No. of trials:3")
    print("2) Medium")
    print("\t Limit:[1-100]")
    print("\t No. of trials:7")
    print("3) Hard")
    print("\t Limit:[1-1000]")
    print("\t No. of trials:15\n")

def choose_game_level():
    x = input("Choose Game Level: ")
    print("")
    return x.strip()

def set_game_settings(x):
    global max_trials
    global limit 

    x = x.lower()

    if x == 'easy':
        max_trials = 3
        limit = 10
    
    elif x == 'medium':
        max_trials = 7
        limit = 100

    elif x == 'medium':
        max_trials = 15
        limit = 1000

    else:
        print("Invalid Choice")
    
def play_game():
    
    global user_trials , max_trials
    
    number = random.randint(0,limit)

    while user_trials < max_trials:

        user_input = int(input("I have a hidden number, guess it : "))

        user_trials += 1

        if user_input == number:
            print(f"You got it successfully in {user_trials} trials")
            break

        elif user_input < number:
            print("No, Increase")

        else:
            print("No, Decrease")

        if user_trials == max_trials:
            print("You couldn't guess the number")

def replay():
    x = input("Do you want to try again? (Yes/No) ").lower().strip()

    if x == 'yes':
        return True
    
    else:
        print("Good bye, see you soon")
        return False
    
def launch_game():
    play = True

    Greeting()

    while play:
        show_game_levels()
        set_game_settings(choose_game_level())
        play_game()
        play = replay()