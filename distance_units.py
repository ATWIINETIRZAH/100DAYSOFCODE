#In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized

feet=int(input("Enter measurement in feet: "))

inches=0.08 * feet
yards= 3 * feet
miles= 5280 * feet

print(f"There are {inches} inches in {feet} feet")

print(f"There are {yards} yards in {feet} feet")

print(f"There are {miles} miles in {feet} feet")