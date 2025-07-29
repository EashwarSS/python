import random

word_list = ["Eashwar", "Shravika", "Mounika", "Anirudh"]

chosen_word = random.choice(word_list).lower()
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

# A placeholder is a way to reserve space for a value that will be supplied later. 
# Placeholders are commonly used in string formatting, function definitions, loops, or to create empty variables or blocks of code. 

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    # Add guessed letter if not already stored
    if guess not in correct_letters:
        correct_letters.append(guess)
        # .append() adds one item at a time
    
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    
    if "_" not in display:
        print("Congratulations! You guessed the word:", chosen_word)
        game_over = True
