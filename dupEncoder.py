'''
The goal of this exercise is to convert a string to a new string where each character 
in the new string is "(" if that character appears only once in the original string, or 
")" if that character appears more than once in the original string. Ignore capitalization 
when determining if a character is a duplicate.
'''
def duplicate_encode(word):
    
    word = str.lower(word)
    palabra_choneta = ""

    for letter in word:
        if word.count(letter) > 1:
            palabra_choneta += ")"
        else :
            palabra_choneta += "("

    return palabra_choneta
        
word = "apples"

print(duplicate_encode(word))