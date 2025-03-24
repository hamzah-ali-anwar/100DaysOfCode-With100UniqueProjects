# write a program to translate a message into secret code language. Use
# the rules below to translate normal English into secret code language

# Coding:
# if the word contains at least 3 characters, remove the first letter
# and append it at the end, now append three random characters at the
# starting and the end, else simply reverse the string

# Decoding:
# If the word contains less than 3 characters, reverse it, else remove
# 3 random characters from start and end. Now remove the last letter and
# append it to the beginning

import random # to pick random letters
import string # to get all upper/lowercase letters

def encode(word): # define function
    if len(word) < 3:
        return word[::-1]
    
    first_letter = word[0]
    new_word = word[1:] + first_letter

    random_chars = ''.join(random.choices(string.ascii_letters, k=3))
    return random_chars + new_word + random_chars


def decode(encoded_word):
    if len(encoded_word) < 3:
        return encoded_word[::-1]
    
    core_word = encoded_word[3:-3]
    last_letter = core_word[-1]
    return last_letter + core_word[:-1]

original_word = "hello"
encoded_word = encode(original_word)
decoded_word = decode(encoded_word)

print(f"Original: {original_word}")
print(f"Encoded: {encoded_word}")
print(f"Decoded: {decoded_word}")