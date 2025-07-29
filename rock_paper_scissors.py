import random

# Define choices and ASCII art for each
options = ["rock", "paper", "scissors"]

ascii_art = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Get user input
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Validate input
if user_choice not in options:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    # Get computer's random choice
    computer_choice = random.choice(options)

    print(f"\nYou chose: {user_choice}")
    print(ascii_art[user_choice])

    print(f"Computer chose: {computer_choice}")
    print(ascii_art[computer_choice])

    # Determine the result
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
    else:
        print("You lose!")