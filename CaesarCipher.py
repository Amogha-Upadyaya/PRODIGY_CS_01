def CaesarCipher(text, shift, mode=""):
    Alpha = "abcdefghijklmnopqrstuvwxyz"
    Caps = Alpha.upper()
    result = ""
    
    if mode == "encrypt":
        if char.isalpha():
            for char in text:
                Index = Alpha.find(char.lower()) if char.islower else Caps.find(char)
                NewIndex = (Index+shift)%26
                NewChar = Alpha[NewIndex] if char.islower() else Caps[NewIndex]
        else:
            NewChar = char
        result += NewChar
    
    if mode == "decrypt":
        result = CaesarCipher(result, -shift)
    
    return result