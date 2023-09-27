# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.
# Hint: One foot is 12 inches. One inch is 2.54 centimeter

feet=int(input("Enter number of feet: "))

inches=int(input("Enter your inches: "))


#feet in cm
print("Feet in cm:",feet*(2.54 * 12))

#inches in cm
print("Inches in cm: ",inches * 2.54)