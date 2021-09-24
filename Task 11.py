#takes time and finds how many seconds there are


hours = int(input("please input the hours"))
minutes = int(input("please input the minutes"))
seconds = int(input("please input the seconds"))

#converts hours into seconds and minutes into seconds and adds those values with the seconds
print((hours * 3600) + (minutes *60) + seconds, "seconds")

## ACS Was the input not in the form mhh:mm:ss .. nonetheless it works well.