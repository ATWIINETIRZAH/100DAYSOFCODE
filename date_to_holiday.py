#Write a program that reads a month and day from the user. If the month and day
# match one of the holidays listed previously then your program should display the
# holiday’s name. Otherwise your program should indicate that the entered month and
# day do not correspond to a fixed-date holiday.

month=input("Enter name of the month: ")
date=int(input("Enter name of the day: "))

if month=="January" and date==1:
    print("The holiday is New Year's")
elif month=="July" and date==1:
    print("The holiday is Canada day")
elif month=="December" and date==25:
    print("Holiday is Christmas day")
else:
    print("Not a holiday date")
