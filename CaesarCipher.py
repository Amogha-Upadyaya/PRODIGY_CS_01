def CC(text, shift, mode=""):
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
    
    if mode == "decrypt":
        result = CC(result, -shift)
    
    return result
