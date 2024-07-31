# Day 8: My Caesar Cipher

import ceasar_cipher
print(ceasar_cipher.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
try_again = 1


# Combining Both Decrypt and Encrypt into 1 Function
def caesar(plain_text, shift_amount, direction):
    the_coded_word = ""
    text_list = list(plain_text)
    for a_letter in text_list:
        is_it_a_letter = False
        for letter in alphabet:
            if a_letter == letter:
                is_it_a_letter = True
                if direction == "encode":
                    a_letter = alphabet.index(letter) + shift_amount
                    if a_letter > 25:
                        a_letter -= 26
                    the_coded_word += alphabet[a_letter]
                if direction == "decode":
                    a_letter = alphabet.index(letter) - shift_amount
                    if a_letter < 0:
                        a_letter += 26
                    the_coded_word += alphabet[a_letter]
        if not is_it_a_letter:
            the_coded_word += a_letter

    print(f"The {direction}d word is {the_coded_word}")


while try_again == 1:
    print("")
    encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    print("")
    caesar(text, shift, encode_or_decode)
    try_again = int(input("Would you like to try again? Enter 1 For Yes or 2 For No: "))
print("Thanks for playing! Please come back soon :3")
