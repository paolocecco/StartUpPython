#takes an input between one and ten, then the first 10 values of that numbers times tables

num = int(input("please enter a number between one and ten"))
while num <1 or num >10:
    num = int(input("please enter a number between one and ten"))
#endwhile
counter = 1
#prints the first 10 times tables for the input number
while counter > 0 and counter < 11:
    print(num*counter , ",")
    counter = counter + 1
#endwhile