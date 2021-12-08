# Instructions :
#
# Create a class called TextModification that inherits from Text.
# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Now, use the provided txt file and try using the class you created above.
# Note: Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

import string, re
class Text:
    def __init__(self, text: str):
        self.text = text

    def word_frequency(self, word: str):
        occurences = self.text.count(word)
        return occurences

    def most_common_words(self):
        frequency = 0
        for word in self.text:
            if self.word_frequency(word) > frequency:
                frequency = self.word_frequency(word)
                return word

    def unique_words(self):
        list_of_words = []
        for word in self.text:
            if self.word_frequency(word) == 1:
                list_of_words.append(word)
            print(list_of_words)

class TextModification(Text):
    def without_punctuation(self):
        new_text = re.sub(r'[^\w\s]', '', self.text)
        return new_text

    def no_stopwords(self):
        with open('the_stranger.txt') as file:
            stopwords_list = file.read().split()
            new_list = [i for i in self.text.split() if i not in stopwords_list]
            print(' '.join(new_list))

with open('C:/Users/lejai/Documents/MyWebSites/DevInst/DI_Bootcamp/Week10/Day4/DailyChallenge/the_stranger.txt') as f:
    file_text = f.read()

analysis = Text(file_text)

