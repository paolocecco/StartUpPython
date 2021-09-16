#create a caeser cypher

sent = str(input("please input a sentence to cypher"))

shift = 3

encryption = ""
#loops through every letter in the input sentence
for c in sent:
    #if the letter is lowercase
    if c.islower():
        #ord function gets the unicode number of the letter
        c_unicode = ord(c)
        #finds the difference between the unicode of the letter compated to the letter a
        c_index = ord(c) - ord("a")
        #performs the shift of the letter in unicode
        new_index = (c_index + shift) % 26
        #converts unicode to character
        new_unicode = new_index + ord("a")
        new_character = chr(new_unicode)
        #appends new character to encrypted string
        encryption = encryption + new_character
    #endif
#next
print(encryption)