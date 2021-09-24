#asks to input a number between 1 and 3
num = int(input("input a number between 1 and 3"))
while num <1 or num >3:
    #reasks for number input until in correct range
    num = int(input("input a number between 1 and 3"))
#endwhile
print("You have selected the option" , num)


## ASC - Good work