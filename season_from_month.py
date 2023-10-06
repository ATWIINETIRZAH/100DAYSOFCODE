#Create a program that reads a month and day from the user. The user will enter
# the name of the month as a string, followed by the day within the month as an
# integer. Then your program should display the season associated with the date that
# was entered.

month1=input("Enter month of the year: ")
date1=int(input("enter the date of the month: "))

def get_season(month, day):
    if (month == 3 and day >= 20) or (month > 3 and month < 6) or (month == 6 and day <= 20):
        return "Spring"
    elif (month == 6 and day >= 21) or (month > 6 and month < 9) or (month == 9 and day <= 22):
        return "Summer"
    elif (month == 9 and day >= 23) or (month > 9 and month < 12) or (month == 12 and day <= 21):
        return "Fall"
    else:
        return "Winter"


# Define a dictionary to map month names to their numerical representation
month_dict = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

# Convert the month string to its numerical representation
if month1 in month_dict:
    month = month_dict[month1]
    # Check if the entered month is valid
    if month >= 1 and month <= 12:
        season = get_season(month, date1)
        print(f"The season associated with {month1} {date1} is {season}.")
    else:
        print("Invalid month entered. Please enter a valid month.")
else:
    print("Invalid month entered. Please enter a valid month.")
