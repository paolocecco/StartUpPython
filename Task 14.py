#inputs a string then prints it out in reverse

#inputs a string
sent = str(input("please input a string"))
#finds the length of the sentence
sentlength = len(sent)
#reverses the characters of the string
slicedsent = sent[sentlength::-1]
print(slicedsent)