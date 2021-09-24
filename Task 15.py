#plays rock paper scissors with user input and randomly chosen opposition input

strike = (input("please enter either R (rock), P (paper) or S (scissors)"))

while strike != "R" or strike != "P" or strike != "S":
    print("Please input a valid strike")
    strike = (input("please enter either R (rock), P (paper) or S (scissors)"))
#endwhile

import string
import random
random.choice(string.ascii_letters)

## ACS This didn't seem to allow valid inputs