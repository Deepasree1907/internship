import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "scissors" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if player_choice not in choices:
            print("Invalid choice. Please choose from rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print("Computer chose:", computer_choice)
        
        winner = determine_winner(player_choice, computer_choice)
        print(winner)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
