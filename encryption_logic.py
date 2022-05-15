from alphabet import alphabet


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter

    print(f"The {cipher_direction}d text is {end_text}")


def encryptor():
    should_continue = True
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        restart = input("Type 'yes' if you would like to continue, otherwise 'no' \n")
        if restart == "no":
            should_continue = False
            print("Adios")
