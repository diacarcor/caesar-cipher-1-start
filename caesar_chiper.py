import alphabet

def encrypt(input_text,shift_amount):
    encoded_text = ""
    for character in input_text:
        position = alphabet.alphabet_list.index(character) 

        new_position = position + shift_amount

        if new_position >=  alphabet.alphabet_len:
            new_position -= alphabet.alphabet_len
        
        encoded_text += alphabet.alphabet_list[new_position]
    
    print("The encoded text is " + encoded_text)

def decrypt (input_text,shift_amount):
    plain_text = ""

    for character in input_text:
        position = alphabet.alphabet_list.index(character) 

        new_position = position - shift_amount

        if new_position < 0:
            new_position += alphabet.alphabet_len

        plain_text += alphabet.alphabet_list[new_position]

    print("The decoded text is " + plain_text)
