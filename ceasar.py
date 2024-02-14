# this line defines all the letters in the alphabet
letters= "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext, key):#defines the encrypt function taking two parameters plaintext and key
    ciphertext= '' #initiates empty string ciphertext to store encrypted text 
    for letter in plaintext:#begins a loop
        letter = letter.lower() #converts each character to lowercase just incase uppercase is used
        if not letter == ' ': #checks that there are no spaces
            index = letters.find(letter) #finds the index characters used in the string
            if index == -1: #checks if letters are not found in the letter string
                ciphertext += letter #if letters are not found  it is added to the ciphertext as is
            else:
                new_index = index + key #calculates the new index by shifting the according to the enncryption key
                if new_index >= 26: #checks if index is within the alphabet
                    new_index -= 26 #checks if index is beyond the alphabet
                ciphertext += letters[new_index] #letter are added to the new cipher string witht the new indec
    return ciphertext #returns final encrypted text
# decrypt fundtion is very similar to the encrypt function above I will highlight the few differences
def decrypt(ciphertext, key):#the two parameters are ciphertext and the decryption key 
    plaintext= '' #initiates the empty string that will store the decrypted text
    for letter in ciphertext: #the loop begins with ciphertext, throughout this block of code we swapped cipher text with plaintext as that is the output we are expecting
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key # calculates the shifting index subtracting the key rather than adding it as in the encrypt block
                if new_index < 0: # checks if new index is 0, as an output is expected within 26
                    new_index += 26 #if 0 it adds the alphabet within 26 characters
        plaintext += letters[new_index] #the character in the the new_index is added to the plaintext
    return plaintext #returns the decrypted message

#intro to ther cipher program
print()
print("*** CEASAR CIPHER PROGRAM ***")
print()

#prompts user to either encrypt or decrypt and takes user input while converting it to lower case 
print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

#if e is chosen that means encrypt mode is selected, calling the encrypt function and printing ciphered text
if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26):' ))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

#if d is chosen that means decrypt mode is selected, calling the decrypt function and printing plain text
if user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26):' ))
    text = input('Enter the text to decrypt: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT:{plaintext}')
