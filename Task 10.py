#finds the number of words in the sentence input

sent = str(input("please enter a sentence"))
#splits the string into a single character per word
wordlist = sent. split()
#counts the number of characters, to define the number of words
wordnum = len(wordlist)
print(wordnum)

## ACS OK The use of split has helped here. 