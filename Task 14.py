#inputs a string then prints it out in reverse

#inputs a string
sent = str(input("please input a string"))
#finds the length of the sentence
sentlength = len(sent)
#reverses the characters of the string
slicedsent = sent[sentlength::-1]
print(slicedsent)

## ACS Good work You might have used a loop and not the python-specific ::-1 function/operator. 