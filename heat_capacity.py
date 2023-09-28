#The amount of energy required to increase the temperature of one gram of a material
# by one degree Celsius is the material’s specific heat capacity, C. The total amount
# of energy required to raise m grams of a material by ∆T degrees Celsius can be
# computed using the formula:
# q = mC∆T.
# Write a program that reads the mass of some water and the temperature change
# from the user. Your program should display the total amount of energy that must be
# added or removed to achieve the desired temperature change.
# Hint: The specific heat capacity of water is 4.186 J
# g
# ◦C
# . Because water has a density of 1.0 gram per millilitre, you can use grams and millilitres interchangeably
# in this exercise.
# Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using units of kilowatt hours rather than Joules. In this
# exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
# your program to compute the cost of boiling water for a cup of coffee.

mass_of_water=int(input("Please enter the mass of water: "))

temperature_change=int(input("Please enter the temperature change: "))

C=4.186

q=mass_of_water * C * temperature_change  

print(f"The total amount of energy is {q} Joules.")

joules_to_kwh=2.7*10**-7*q

elec=joules_to_kwh* 8.9

print(f"Cost boiling water is:",elec,"")

