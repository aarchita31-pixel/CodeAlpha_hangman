import random

# Step 1: Define a list of words
word_list = ["apple", "banana", "grape", "orange", "peach"]

# Step 2: Choose a random word
secret_word = random.choice(word_list)

# Step 3: Initialize game state
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Step 4: Main game loop
print("🎮 Welcome to Hangman!")
while wrong_guesses < max_wrong_guesses and not all(letter in guessed_letters for letter in secret_word):
    # Display current progress without using a function
    print("\nWord:", end=" ")
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in secret_word:
        guessed_letters.append(guess)
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        guessed_letters.append(guess)
        print("❌ Wrong!")

# Step 5: End of game
if set(secret_word).issubset(set(guessed_letters)):
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n😢 Game over! The word was:", secret_word)
