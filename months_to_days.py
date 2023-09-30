#The length of a month varies from 28 to 31 days. In this exercise you will create
# a program that reads the name of a month from the user as a string. Then your
# program should display the number of days in that month. Display “28 or 29 days”
# for February so that leap years are addressed

month=input("Enter name of the month: ")

if month=="January":
    print("There are 31 dyas in January")
elif month=="February":
    print("There are 28 or 29 days in February")
elif month=="March":
    print("There are 31 days in March")
elif month=="April":
    print("There are 30 days in April")
elif month=="May":
    print("There are 31 days in May")
elif month=="June":
    print("There are 30 days in June")
elif month=="July":
    print("There are 31 days in July")
elif month=="August":
    print("There are 31 days in August")
elif month=="September":
    print("There are 30 days in September")
elif month=="October":
    print("There are 31 days in October")
elif month=="November":
    print("There are 30 days in November")
elif month=="December":
    print("There are 31 days in December")