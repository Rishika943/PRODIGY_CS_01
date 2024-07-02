def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

message = input("Enter the message to encrypt or decrypt: ")
shift_value = int(input("Enter the shift value: "))

encrypted_message = caesar_cipher(message, shift_value)
decrypted_message = caesar_decipher(encrypted_message, shift_value)

print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
