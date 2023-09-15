#Create a program that reads the length and width of a farmer’s ﬁeld from the user in feet. 
#Display the area of the ﬁeld in acres.

length=int(input("Enter the length of your field in feet: "))
width=int(input("Enter the width of your field in feet: "))

Area_in_ft=int(length * width)
print("The area of your field is",Area_in_ft,"square feet.")

Area_in_acres=int(Area_in_ft/43600)
print("your farm is",Area_in_acres,"acres.")

