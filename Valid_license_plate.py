#In a particular jurisdiction, older license plates consist of three uppercase letters
# followed by three numbers. When all of the license plates following that pattern had
# been used, the format was changed to four numbers followed by three uppercase
# letters.
# Write a program that begins by reading a string of characters from the user. Then
# your program should display a message indicating whether the characters are valid
# for an older style license plate or a newer style license plate. Your program should
# display an appropriate message if the string entered by the user is not valid for either
# style of license plate.

license=input("Enter your license plate: ")

#here i used the .isalpha and isdigit function that check the alphabetical and numerical parameters
if len(license)==6 and license[:3].isalpha() and license[3:].isdigit():
    print("This is valid for an older style license plate")
elif len(license)==7 and license[:3].isalpha() and license[4:].isdigit():
    print("This is valid for a newer style license plate")
else:
    print("This is not valid for either newer or older style license plates")


