from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']

alpha_length = len(alphabet)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = []
    for i in range(len(start_text)):
        if start_text[i] not in alphabet: 
            end_text.append(start_text[i]) 
        else: 
            Index = alphabet.index(start_text[i])
            if cipher_direction == 'encode':
                Index += shift_amount
                if Index >= alpha_length:
                    Index = Index%(alpha_length)
            elif cipher_direction == 'decode':
                Index -= shift_amount
                if Index < 0:
                    Index += alpha_length       # + as Index is already negative
            end_text.append(alphabet[Index])
    print(f"The {cipher_direction}d text: {''.join(end_text)}")


# OR

# def encrypt(plain_text, shift_amount):
#     eoutput = [] 
#     for i in range(len(plain_text)):
#         if plain_text[i] != " ":
#             Index = alphabet.index(plain_text[i])
#             Index += shift_amount
#             eoutput.append(alphabet[Index])
#         else:
#             eoutput.append(" ")
#     print(f"The encoded text is {''.join(eoutput)}")

# def decrypt(encrypted_text, shift_amount):
#     doutput = []
#     for i in range(len(encrypted_text)):
#         if encrypted_text[i] != " ":
#             Index = alphabet.index(encrypted_text[i])
#             doutput.append(alphabet[Index])
#         else:
#             doutput.append(" ")
#     print(f"The decoded text is {''.join(doutput)}")


should_end = False
while not should_end:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if (direction == 'encode' or direction == 'decode'):
        caesar(text, shift, direction)    
    else:
        print("Invalid Input !")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == 'no':
        should_end = True
        print("GoodBye")