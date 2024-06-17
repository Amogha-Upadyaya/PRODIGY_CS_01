def CCEncrypt(text, shift, mode=""):
    Alpha = "abcdefghijklmnopqrstuvwxyz"
    Caps = Alpha.upper()
    result = ""
    
    if mode == "encrypt":
        for char in text:
            if char.isalpha():
                Index = Alpha.find(char.lower()) if char.islower else Caps.find(char)
                NewIndex = (Index+shift)%26
                NewChar = Alpha[NewIndex] if char.islower() else Caps[NewIndex]
            else:
                NewChar = char
            result += NewChar
    return result

def CCDecrypt(text, shift, mode=""):
    if mode == "decrypt":
        result = CCEncrypt(text, -shift)
    return result