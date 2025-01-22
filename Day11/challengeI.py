# Challenge 3: Guess the Secret Word
''' Write a program that repeatedly asks the user to guess a secret word until they guess it correctly.

Use a break statement to exit the loop when the correct word is guessed.
If the user types "quit," exit the loop immediately without revealing the secret word.
'''

secret_word = "secret"
user_input = input("Guess a secret word or type quit to exit the loop: ")

while user_input != secret_word:
    if user_input == "quit":
        print("Exiting the loop")
        break
    user_input = input("Guess a secret word or type quit to exit the loop: ")

if user_input == secret_word:
    print(f"That's correct, {secret_word} is the secret word")