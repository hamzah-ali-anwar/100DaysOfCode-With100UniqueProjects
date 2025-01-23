# Challenge 3: Palindrome Checker
''' Write a function called is_palindrome that checks whether a given string is a palindrome 
(reads the same forward and backward). Ignore case and non-alphanumeric characters.
'''

import re

def is_palindrome(s):
    clean_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return clean_string == clean_string[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("Madam"))  # Output: True
