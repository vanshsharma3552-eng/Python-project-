import random

# Available choices
choices = ["rock", "paper", "scissors"]

# Initialize scores
user_score = 0
computer_score = 0

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "user"
    else:
        return "computer"

def display_scores():
    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

def main():
    global user_score, computer_score
    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.\n")

    while True:
        user_choice = input("Your choice: ").strip().lower()

        if user_choice == 'exit':
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print(" Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f" Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "tie":
            print(" It's a tie!")
        elif result == "user":
            print(" You win this round!")
            user_score += 1
        else:
            print(" Computer wins this round!")
            computer_score += 1

        display_scores()

        # Ask to play again
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\n Final Scores:")
            display_scores()
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
