'''
Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
'''

def spin_words(sentence):
    
    phrase = ""

    for word in sentence.split(" "):
        if len(word) >= 5:
            phrase += word[::-1] + " "
        else:
            phrase += word + " "

    return phrase
'''
def spin_words(sentence):
    return " ".join([word[::-1] if len(word)>=5 else word for word in sentence.split()])
'''

sentence = "more only five all will the like desrever only more words"
#sentence = "test1 test test"

print(spin_words(sentence))