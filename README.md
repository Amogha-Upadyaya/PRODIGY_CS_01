# PRODIGY_CS_01
The following repository documents the Task-01 assigned during my Cybersecurity Internship at Prodigy InfoTech

## Aim
Create a Python program that can encrypt and decrypt text using the Caesar Cipher Algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

# Caesar Cipher Algorithm
## Encryption
1. Take plaintext message (string) and shift value (integer between 1 and 25) as input
2. For every character in the plaintext, check if the character is an alphabet.
3. Convert the character to its numerical position in the alphabet
4. Add the shift value to the numerical position
5. Apply the modulo operation with 26 to ensure the result stays within the alphabetical range. Accounts for wrapping around the alphabet.
6. Convert the resulting number back to its corresponding character.
7. Output the encrypted ciphertext message

## Decryption
1. Take cipher text message (string) and shift value (key for encryption) as input
2. For every character in the plaintext, check if the character is an alphabet.
3. Convert the character to its numerical position in the alphabet.
4. Subtract the shift value from the numerical position
5. Apply the modulo operation with 26 to ensure the result stays within the alphabetical range
6. Conver the resulting number back to its corresponding character
7. Output the decrypted plaintext message
