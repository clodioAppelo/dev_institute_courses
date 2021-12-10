# this file must contain UI
#menu offering input word or exit
# only a single word is allowed, show error if more
#only alphabetic character allowed
#whitespaced should be remove from start and end

#show all possible anagrams to user's word
# create anagram checker
#diplay info about word in friendly format

import anagram_checker


def main():
    active = True

    while active:
        option = input("Please enter word to check anagrams or press e(X)it: \n")
        option = option.strip() # removes white spacing
        if option.lower() == "x": # user's exit
            active = False
        elif len(option.split()) > 1:
            print('Only one word is accepted, please enter a word')
            continue
        elif not option.isalpha(): # if input is not alphabetic word
            print('Please enter only alphabetic letter')
            continue
        else:
            func_checker = anagram_checker.AnagramChecker()
            if not func_checker.is_valid_word(option):
                print('please enter a valid word')
                continue
            else:
                anagram_list = func_checker.get_anagrams(option)
                print(f"Your given word {option} \n It's a valid English word \n Anagrams for your given word: {' '.join(anagram_list)}")


main()

