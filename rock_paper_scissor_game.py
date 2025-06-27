import random
options = ['rock', 'paper', 'scissor']
computer_option = random.choice(options)
user_option = input("Enter Option rock, paper, scissor: ").lower()
game_over = False

while not game_over:
    if user_option == computer_option:
        print("Game Tie")
        user_option = input("Enter Agian: ").lower()
    elif user_option == 'rock':
        if computer_option == 'scissor':
            print("computer option was",(computer_option))
            print("You win")
            game_over = True
        else:
            print("You lose")
            user_option = input("Enter Agian: ").lower()
    elif user_option == 'paper':
        if computer_option == 'rock':
            print("computer option was",(computer_option))
            print("You win")
            game_over = True
        else:
            print("You lose")
            user_option = input("Enter Agian: ").lower()
    elif user_option == 'scissor':
        if computer_option == 'paper':
            print("computer option was",(computer_option))
            print("You win")
            game_over = True
        else:
            print("You lose")
            user_option = input("Enter Agian: ").lower()
    else:
        print("Please enter valid option")
        user_option = input("Enter Agian: ").lower()

