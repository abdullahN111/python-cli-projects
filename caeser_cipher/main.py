
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + shift_key)%26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char
             
    print(f"\nHere is the encrypted message: {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - shift_key)%26
            plain_text += alphabets[new_position]
        else:
            plain_text += char
            
    print(f"\nHere is the decrypted message: {plain_text}")

wanna_end = False

while not wanna_end:

    what_to_do = input("\nType 'encrypt' to encrypt a message, or 'decrypt' to decrypt a message: \n")
    text = input("\nEnter the message:\n").lower()
    shift = int(input("\nEnter shift key:\n"))

    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_key=shift)
        
    elif what_to_do == "decrypt":
        decryption(cipher_text=text, shift_key=shift)

    else:
        print("Invalid input. Please try again.")
        
    play_again = input("\nDo you want to go again? Type 'yes' or 'no': ").lower()
        
    if play_again == "no":
        wanna_end = True
        print("Goodbye!")
        
    elif play_again == "yes":
        wanna_end = False
        
    else:
        print("Invalid input. Please try again.")
        