"""
This is a python program which is a function called num2words() with only one parameter
and used to convert a given number (between 0 and 99) as integer to text in English.
"""
#
# (C) AramBakir@github
#
# Created on: November 13, 2022
# Last update: November 13, 2022
#
# Distributed under the terms of the MIT license.
#


def num2words(num):

    # Declare and initialize "onesArr" and "onesStr" arrays
    onesArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    onesStr = ["zero", "one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]

    # We don't need to create an array containing 10 - 19 as Integer;
    # just assume that the first digit is always 1
    # and reuse "onesArr" array to get the second digit. Got it? :)
    _10_to_19_Str = ["ten", "eleven", "twelve", "thirteen", "fourteen",
                     "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    # All "None" elements in "tensArr" and "tensStr" arrays are just used to ignore those indexes
    tensArr = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    tensStr = [None, None, "twenty", "thirty", "forty", "fifty",
               "sixty", "seventy", "eighty", "ninety"]

    # Split inserted "num" integer into "numArr" array
    # num = 25, numArr = [2,5]
    numArr = [int(x) for x in str(num)]

    # Take the "numArr" length
    numArr_length = len(numArr)

    # If "numArr_length" was equal to 1, print between "zero" and "nine"
    if (numArr_length == 1) and (numArr[0] in onesArr):
        x = onesStr[numArr[0]]
        print(x)

    # If "numArr" first digit was equal to 1, print between "ten" and "nineteen"
    elif (numArr_length == 2) and (numArr[0] == 1) and (numArr[1] in onesArr):
        x = _10_to_19_Str[numArr[1]]
        print(x)

    # If "numArr_length" was equal to 2, print between "twenty" and "ninety-nine"
    elif (numArr_length == 2) and (numArr[0] in tensArr) and (numArr[1] in onesArr):

        # For example: assume num = 25
        x = tensStr[numArr[0]]  # x is the first digit; x = 2
        y = onesStr[numArr[1]]  # y is the second digit; y = 5

        # Do not print "zero" for 10, 20, 30 etc... (i. e. twenty zero) =(
        if (y == "zero"):
            print(x)  # Just print twenty
        else:
            # Input: 25, Output: twenty-five
            print(x, "-", y, sep="")

    else:
        # If the "numArr_length" is more than 2, then show an alert
        print("Sorry! Your number must be between 0 and 99. :( Try again!")

    return ""


# Test the function
result = num2words(0)
result = num2words(10)
result = num2words(25)
result = num2words(99)
result = num2words(100)

print(result)
