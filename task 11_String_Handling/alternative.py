"""  
Practical Task 1:
1. Write a program that reads in a string and makes each alternate character into an upper case character and each other alternate character a lower case character.

2. Now, try starting with the same string but making each alternative word
lower and upper case.
e.g. The string: “I am learning to code” would become “i AM learning
TO code”.
Tip: Using the split() and join() functions will help you here.
"""

sentence = input("Write your sentence here:")
#list to storage the character of the sentences after the alternate process
sentence_builder = ""

#for each character(s) in the sentence:
for s in range(len(sentence)):

#if the index of the character is odd, alternate to uppercase:
    if s % 2 == 1 :
        sentence_builder += sentence[s].upper()
    
    else:
        sentence_builder += sentence[s].lower()
#Print the result with alternative character 
print(sentence_builder)

# function to split the sentence in list of word
word_sentence = sentence.split(" ")

# if the index of the word is odd, alternate the word to uppercase
for index in range(len(word_sentence)):
    if index % 2 == 1:
        word_sentence[index] = word_sentence[index].upper()
    
    else:
        word_sentence[index] = word_sentence[index].lower()

final_sentence = " ".join(word_sentence)
# Print the result with alternative word
print(final_sentence)



