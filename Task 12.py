#finds the factors of an input number

num = int(input("please input a number"))

i = 2
#tests every number between 2 and the number input to check if it is a factor
while i > 1 and i < num:
    if num % i == 0:
        print(i)
    i = i + 1