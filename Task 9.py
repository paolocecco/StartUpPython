#takes three numbers and prints from highest to lowest

num1 = int(input("enter the first integer"))
num2 = int(input("enter the second integer"))
num3 = int(input("enter the third integer"))

#finds the order of the sixe of the three numbers
if num1 > num2 and num2 > num3:
    print(num1, num2, num3)
elif num1 > num3 and num3 > num2:
    print(num1, num3, num2)
elif num2 > num1 and num1 > num3:
    print(num2, num1, num3)
elif num2 > num3 and num3 > num1:
    print(num2, num3, num1)
elif num3 > num1 and num1 > num2:
    print(num3, num1, num2)
elif num3 > num2 and num2 > num1:
    print(num3, num2, num1)
#endif

## ACS Good but possibly not the most efficient solution. if there were 6 numbers this would get very long!