import base64

text = "Python is fun!"
encoded_text = base64.b64encode(text.encode()).decode()
print("Encoded:", encoded_text)

decode_text = base64.b64decode(encoded_text).decode()
print("Decoded:", decode_text)