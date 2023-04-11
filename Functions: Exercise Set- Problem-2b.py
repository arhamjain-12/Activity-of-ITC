

"""
(b) How one can check if the restriction is on a number of words rather than letters?
Write a function that allows a message with only 30 words.
"""
def chit_word(message):
    word=message.split()
    if len(word) <=30:
        return message
    else:
        return 'message is greater then 30 words'
        
        
b=input()
a=chit_word(b)
print(a)