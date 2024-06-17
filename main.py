import CaesarCipher # Import the CaesarCipher Module
while True:
    print("\nCASER CIPHER")
    print("1. Encrypt\n2. Decrypt\n3. Exit")
    opt = int(input("Enter the index number corresponding your choice: ")) # Get user choice

    if opt == 1:
        PlainText = input("Enter the message to encrypt: ")
        try:
            Key = int(input("Enter the shift value (key): ")) # Get key (shift value)
        except ValueError:
            print("Invalid key. Please enter an Integer.")
            continue # Skip to next iteration if key is not an integer

        CipherText = CaesarCipher.CCEncrypt(PlainText, Key, mode="encrypt")
        # Print Encrypted/Cipher Message
        print(f"Encrypted Message: %s" % CipherText)
    
    elif opt == 2:
        CipherText = input("Enter the message to decrypt: ")
        try:
            Key = int(input("Enter the shift value (key): ")) # Get key (shift value)
        except ValueError:
            print("Invalid key. Please enter an integer.")
            continue # Skip to next iteration if key is not an integer

        PlainText = CaesarCipher.CCDecrypt(CipherText, Key, mode="decrypt")
        print(f"Decrypted Message: %s" % PlainText) # Print Decrypted/PlainText Message
    
    elif opt == 3:
        break # Exit the loop on option 3

    else:
        print("Invalid choice. Try Again.")