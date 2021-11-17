# Instructions
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some
# fixed number of positions down the alphabet.
#
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method
# is named after Julius Caesar, who used it in his private correspondence.
#
# Create a python program that encrypts and decrypts messages with Ceasar cypher, the user entries the
# program, and then the program asks him if he wants to encrypt or decrypt, and then execute
# encryption/decryption on a given message and a given shift.
#
# for letter in text:
#     cypher_text += chr(ord(letter) + 3)

import string
alphabets = string.ascii_lowercase + string.ascii_lowercase
sentence = list(input(" enter your sentence: \n").lower())
what_to_do = input("enter encrypt to ENCRYPT, decrypt to DECRYPT \n").lower()
shift = int(input("enter your shift number from 1 to 25 \n"))
end_program = False

while not end_program:
    # Search through the given text
    if what_to_do == "encrypt":
        for i in range(len(sentence)):
            #get the position of the character in the sentence
            if sentence[i] == " ":
                sentence[i] == " "
            else:
                new_letter = alphabets.index(sentence[i]) + shift
                sentence[i] = alphabets[new_letter]
         # convert the list back to string
        print("".join(map(str, sentence)))
        end_program = True
    elif what_to_do == "decrypt":
        for i in range(len(sentence)):
            if sentence[i] == " ":
                sentence[i] == " "
            else:
                new_letter = alphabets.index(sentence[i]) - shift
                sentence[i] = alphabets[new_letter]
        # convert the list back to string
        print("".join((map(str, sentence))))
        end_program = True
    else:
        decide = input("Invalid entry, try Y for yes, N for no \n").lower()
        if decide == "y":
            sentence = list(input(" enter your sentence: \n").lower())
            what_to_do = input("enter encrypt to ENCRYPT, decrypt to DECRYPT \n").lower()
            shift = int(input("enter your shift number from 1 to 25 \n"))
        else:
            end_program = True





