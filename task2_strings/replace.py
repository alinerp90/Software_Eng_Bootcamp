#Practical Task 2

"""
save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog.”
1.Replace the ! for blank space using replace()
2.Reprint using upper()
3.Reprint in reverse using extendend slice with -1.
"""

sentence= "The!quick!brown!fox!jumps!over!the!lazy!dog."
clean_sentence=sentence.replace('!',' ')
print(clean_sentence)

upper_sentence=clean_sentence.upper()
print(upper_sentence)

reverse_sentence=clean_sentence[::-1]
print(reverse_sentence)

