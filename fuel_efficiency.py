#In the United States, fuel efficiency for vehicles is normally expressed in miles-per gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
#kilometers (L/100 km). Use your research skills to determine how to convert from
#MPG to L/100 km. Then create a program that reads a value from the user in American
#units and displays the equivalent fuel efficiency in Canadian units



fuel_value=int(input("Enter your fuel value in American units(miles per gallon): "))

#1 US mpg = 235.215 L/100km
fuel_value_in_canadian_units=fuel_value*235.215

print("Fuel value in canadian units(Litres per kilometre):",fuel_value_in_canadian_units)


