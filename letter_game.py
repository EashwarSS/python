import random

word_list = ["Eashwar", "Shravika", "Mounika", "Anirudh"]
chosen_word = random.choice(word_list).lower()
print(f"(Debug) The chosen word is: {chosen_word}")  # Remove this line for real gameplay

# Create a list of underscores as the display (one for each letter)
display = ["_"] * len(chosen_word)
correct_letters = []

# Show the initial placeholder
print(" ".join(display))

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    for index in range(len(chosen_word)):
        # If chosen_word is "mounika", then len(chosen_word) is 7, and index goes from 0 to 6.
        if chosen_word[index] == guess:
            # Compares the letter at the current index with the letter the user guessed.
            # Example: if chosen_word is "mounika" and guess is 'o', this checks:
            # chosen_word[0] == 'o' → 'm' == 'o' → ❌
            # chosen_word[1] == 'o' → 'o' == 'o' → ✅
            display[index] = guess
            # If there's a match, update the display list at that same index.

    print(" ".join(display))  # Print the updated placeholder after each guess

    if "_" not in display:
        print("Congratulations! You've guessed the word:", chosen_word)
        game_over = True