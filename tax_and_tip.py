#The program that you create for this exercise will begin by reading the cost of a mealordered at a restaurant from the user. 
#Then your program will compute the tax andtip for the meal. Use your local tax rate when computing the amount of tax owing.
#Compute the tip as 18 percent of the meal amount (without the tax). 
#The output fromyour program should include the tax amount, the tip amount, and the grand total forthe meal including both the tax and the tip. 
#Format the output so that all of the values are displayed using two decimal places

#cost refers to the amount paid by the customer for the meal
cost=int(input("Please enter the cost of your meal: "))

tax=float(0.20 * cost)
tax_round=round(tax,2)

tip=float(0.18 * (cost-(tax)))
tip_round=round(tip,2)

total= float(cost + tax + tip)
total_round=round(total,2)

print("Tax amount: ",tax_round,"Tip amount: ",tip_round,"Grand total: ",total_round)