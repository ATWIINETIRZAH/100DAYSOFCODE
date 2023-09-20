#Pretend that you have just opened a new savings account that earns 4 percent interest
#per year. The interest that you earn is paid at the end of the year, and is added
#to the balance of the savings account. Write a program that begins by reading the
#amount of money deposited into the account from the user. Then your program should
#compute and display the amount in the savings account after 1, 2, and 3 years. Display
#each amount so that it is rounded to 2 decimal places.

amount=int(input("enter your amount of savings: "))
print("The amount deposited is ",amount)


year_1=round(((0.04*amount)+amount),2)
print("Amount in bank after one year is:",year_1)

year2=round((year_1+(0.04*year_1)),2)
print("Amount in bank after two years is:",year2)

year_3=round((year2+(0.04*year2)),2)
print("Amount in bank after three years is:",year_3)

