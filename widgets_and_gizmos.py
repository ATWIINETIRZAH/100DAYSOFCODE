#An online retailer sells two products: widgets and gizmos. Each widget weighs 75
#grams. Each gizmo weighs 112 grams. Write a program that reads the number of
#widgets and the number of gizmos in an order from the user. Then your program
#should compute and display the total weight of the order

num_of_widgets=int(input("Please Enter the number of widgets you would like: "))
num_of_gizmos=int(input("Please Enter the number of gizmos you would like: "))

total_weight=num_of_widgets*75 + num_of_gizmos*112

print("The total weight of your order is",total_weight,"grams.")