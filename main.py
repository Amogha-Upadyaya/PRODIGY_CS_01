import CaesarCipher
while True:
    print("\nCASER CIPHER")
    print("1. Encrypt\n2. Decrypt\n3. Exit")
    opt = int(input("Enter the index number corresponding your choice: "))

    if opt == 1:
        PlainText = input("Enter the message to encrypt: ")
        Key = int(input("Enter the shift value (key): "))

        CipherText = CaesarCipher.CC(PlainText, Key, mode="encrypt")
        print(f"Encrypted Message: %s" % CipherText)
    
    elif opt == 2:
        CipherText = input("Enter the message to decrypt: ")
        Key = int(input("Enter the shift value (key): "))
        PlainText = CaesarCipher.CC(PlainText, Key, mode="decrypt")
        print(f"Decrypted Message: %s" % PlainText)
    
    elif opt == 3:
        break

    else:
        print("Invalid choice. Try Again.")