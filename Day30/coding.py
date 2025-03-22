# Coding is the process of converting human-readable information into
# a different format

message = "HELLO"

morse_code = {
    'H': '....', 'E': '.', 'L': '.-..', 'O': '___'
}

encoded_message = " ".join(morse_code[char] for char in message)
print(encoded_message)