#asks for a three digit integer and displays each unit individually

num = int(input("enter a number between 100 and 999"))
while num <100 or num >999:
    #only accepts numbers in the valid range
    num = int(input("enter a number between 100 and 999"))
#endwhile
print(num // 100 , " hundreds, " , (num//10)%10 , " tens, " , (num%10) , " units.")