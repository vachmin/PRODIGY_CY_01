def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char 
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

encrypted_text = encrypt(text, shift)
print("\nEncrypted Text: ", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Text: ", decrypted_text)


