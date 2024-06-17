def CCEncrypt(text, shift, mode=""):
    Alpha = "abcdefghijklmnopqrstuvwxyz" # Lowercase alphabet string
    Caps = Alpha.upper() # Uppercase alphabet string derived from lowercase)
    result = "" # Initialize empty string to store encrypted text
    
    if mode == "encrypt": # Check if mode is encryption
        for char in text:
            if char.isalpha(): # Check if character is alphabetic
                Index = Alpha.find(char.lower()) if char.islower else Caps.find(char) # Find index in appropriate alphabet
                NewIndex = (Index+shift)%26 # Apply shift with modulo 26
                NewChar = Alpha[NewIndex] if char.islower() else Caps[NewIndex] # Get new character from same alphabet
            else:
                NewChar = char # Keep non-alphabetic character unchanged
            result += NewChar # Append new character to encrypted text
            return result # Return the encrypted text

def CCDecrypt(text, shift, mode=""):
    if mode == "decrypt": # Check if mode is decryption
        result = CCEncrypt(text, -shift, mode="encrypt") # Decrypt by calling encryption with negative shift
    return result # Return the decrypted text