import random

def get_user_choice():
    print("\nChoose Rock, Paper, or Scissors")
    choice = input("Your choice: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Your choice: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n🔁 Round {round_number}")
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"\n🧑 You chose: {user}")
        print(f"💻 Computer chose: {computer}")

        result = determine_winner(user, computer)

        if result == "tie":
            print("🤝 It's a tie!")
        elif result == "user":
            print("🎉 You win!")
            user_score += 1
        else:
            print("💀 Computer wins!")
            computer_score += 1

        print(f"\n📊 Score => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\n👋 Thanks for playing!")
            break

        round_number += 1

# Run the game
play_game()
