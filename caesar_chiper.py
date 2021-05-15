alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_length = len(alphabet)
def caesar(input_text, shift_amount, chyper_direction):

    output_text = ""

    if chyper_direction == "decode":
        shift_amount *= -1
    

    for character in input_text:
        if character not in alphabet:
            output_text += character
        else:
            position = alphabet.index(character)

            new_position = position + shift_amount
            
            if (new_position >= alphabet_length) or (new_position <0 ):
                new_position %= alphabet_length
                
            output_text += alphabet[new_position]
        
    print(f"Here's the {chyper_direction}d result: {output_text}\n")
   