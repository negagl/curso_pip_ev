import random

options = ('rock', 'paper', 'scissors')
rules = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}
ascii = {
    'rock': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""",
    'paper': """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)""",
    'scissors': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""
}

# Is a tie?


def isTie(user_choice, cpu_choice):
    # Returns true if the choices are the same
    return (user_choice == cpu_choice)

# Ask if the user wants to play a new game


def newGame():
    while (True):
        again = input('\n\nDo you want to play another match? y/n: ')
        if (again == 'y'):
            print('A new battle is about to start...')
            battle()
        elif (again == 'n'):
            print('Goodbye loser')
            exit()
        else:
            print('Please, select a valid choice (-_-#)')
            continue

# Define the battle rules to see who wins


def seeRules(user_choice, cpu_choice):
    # First we see if the user choice is in the keys(winning side)
    if (rules[user_choice] == cpu_choice):
        print('You win.')
    else:
        print('You loose.')
    newGame()

# Main game logic. Asking for choices and invoking the other functions


def battle():
    while (True):
        print('Select your choice: rock, paper, scissors!!')
        user_opt = input('=>').lower()
        cpu_opt = random.choice(options)

        if (user_opt in options):
            print(
                f'\n\n\nYou chose: {ascii[user_opt]}\n\nCPU chooses: {ascii[cpu_opt]}\n\n')
            if (isTie(user_opt, cpu_opt)):
                print('Tie. Trying again...\n\n\n')
                continue
            else:
                seeRules(user_opt, cpu_opt)
        else:
            print('Hey, dont be cheater, choose a valid choice 🤬')
            continue


# Executing the game
battle()
