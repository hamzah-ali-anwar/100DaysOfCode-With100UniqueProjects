# converting encoded data back inti a readable format

message = "HELLO"

morse_code = {
    'H': '....', 'E': '.', 'L': '.-..', 'O': '___'
}

encoded_message = " ".join(morse_code[char] for char in message)

print("Encoded:", encoded_message)

morse_to_text = {v: k for k, v in morse_code.items()}

decoded_message = "".join(morse_to_text[code] for code in encoded_message.split())

print("Decoded:", decoded_message)