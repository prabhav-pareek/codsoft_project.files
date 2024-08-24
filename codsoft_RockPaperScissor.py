import random

def computer_ch():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    print("\t***Welcome to ROCK, PAPER and SCISSORS!!***")
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    computer_choice = computer_ch()
    print(f"Computer chose: {computer_choice}")
    
    winner = get_winner(user_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")
    
    return winner

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        result = play_round()
        
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        
        print(f"Your Score: {user_score}, Computer's Score: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'no':
            print("Thanks for Playing")
        elif play_again == 'yes':
            play_game()
        else:
            print("Wrong Input!")
            print("Choose either yes or no")
play_game()