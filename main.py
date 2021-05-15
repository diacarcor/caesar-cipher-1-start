import caesar_chiper

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    caesar_chiper.encrypt(input_text = text,shift_amount = shift)
elif direction == "decode":
    caesar_chiper.decrypt(input_text = text, shift_amount = shift)


    
   
