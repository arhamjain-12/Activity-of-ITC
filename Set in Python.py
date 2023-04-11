
"""Problem - I 
sentence = "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drink"
print(verse, "\n")
# split sentence into list of words
sentence_list =  # You will have to fill out the function 
print(sentence_list, '\n')
# convert list to set to get unique words
sentence_set = 
print(sentence_set, '\n')
# print the number of unique words
num_unique = 
print(num_unique, '\n')"""

sentence= "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drink"
A=sentence.split()
print("Verse= ",*A)
print("sentence_list= ",A,"\n")

B=set(A)
print("sentence_set= ",B,"\n")

print("num_unique: ",len(B),"\n")