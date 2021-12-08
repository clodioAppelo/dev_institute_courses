#Exercise 1 – Random Sentence Generator
#
# Description: In this exercise we will create a random sentence generator. We will do this
# by asking the user how long the sentence should be and then printing the generated sentence.
#

# import random, json
#
# words = []
#
#
# def get_words_from_file():
#     with open("sowpods.txt") as f:
#         for line in f.readlines():
#             words.append(line)
#
#
# def get_random_sentence(length: int):
#     sentence = ''.join([random.choice(words) for i in range(length)])
#     print(sentence.lower())
#
#
# def sentence_Generator():
#     print("Hello, this program will generate a random sentence for you!")
#     length = int(input("Choose how long you want your sentence to be. Between 2-20: "))
#     if 1 < length < 21:
#         get_words_from_file()
#         get_random_sentence(length)
#     else:
#         print("Sorry! Incorrect number!")
#
# sentence_Generator()

# -----------------------------------------------------------------------------------------
# Exercise 2
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

import json
sampleJson = {
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}

print(sampleJson['company']['employee']['payable']["salary"])
sampleJson['company']['employee']['birth_date'] = ['3/07/1980']
print(sampleJson['company']['employee'])

json_file = 'file.json'
with open(json_file, 'w') as file_obj:
   json.dump(sampleJson, file_obj, indent=2)
