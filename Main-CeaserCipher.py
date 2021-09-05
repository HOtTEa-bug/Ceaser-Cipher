alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'  ]



def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction=='decode':
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
        
    print(f"The {cipher_direction}d result : {end_text} \n\nMy grandfather told me that I'm very smart! Σd(˘◡˘๑)\n\n")



from art import logo
print(logo)

print("\n\nWELCOME TO CEASER CIPHER! \n\nMy name is Ceaser, and I will be at your service! (◠﹏◠) \n\nBUT LET ME TELL YOU A SECRET. IF YOU FAIL TO ENTER CORRECT INSTRUCTION I WILL FALL ASLEEP! ( ͡ಠ ʖ̯ ͡ಠ) \n\n")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)

        result = input("\nType 'yes' if you want to go again. Otherwise type 'no': ")
        if result == "no":
            should_continue = False
            print("So do we have to say goodbye here?( ಠ ʖ̯ ಠ) \nSee you next time!\(ᵔᵕᵔ)/")
        elif result == "yes":
            print("Bet! You liked my skills! Didn't you? Okay let's continue! ~(^-^)~ \n\n")
        else:
            print("Opps! Looks like you have entered an unknown command! Ceaser has fallen asleep! ᴖ̮ ̮ᴖ ")
            break

    else:
        print("Opps! Looks like you have entered an unknown command! Ceaser has fallen asleep! ᴖ̮ ̮ᴖ ")
        break