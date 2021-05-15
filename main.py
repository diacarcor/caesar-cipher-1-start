import caesar_chiper
from art import logo

print (logo)

is_continue = True

while (is_continue):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction not in ("encode","decode"):
        print("Wrong direction.")
    else:
        caesar_chiper.caesar (input_text = text,shift_amount = shift, chyper_direction = direction)

    want_to_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if want_to_continue == "no":
        is_continue = False
    
   
