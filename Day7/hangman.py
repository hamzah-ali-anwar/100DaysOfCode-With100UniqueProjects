import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"Chosen word: {chosen_word}")  # You might want to remove this line in the final version

word_length = len(chosen_word)
display = ["-"] * word_length
print("".join(display))

game_over = False
guessed_letters = []
lives = 6  # You can adjust this number

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed {guess}. Try another letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Good guess!")
    else:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")

    print("".join(display))
    print(f"Guessed letters: {', '.join(guessed_letters)}")

    if "-" not in display:
        game_over = True
        print("You win!")
    elif lives == 0:
        game_over = True
        print(f"You lose. The word was {chosen_word}.")
