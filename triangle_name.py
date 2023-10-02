#A triangle can be classified based on the lengths of its sides as equilateral, isosceles
# or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user.
# Display a message indicating the type of the triangle.

length1=int(input("Enter length of side a: "))
length2=int(input("Enter length of side b:"))
length3=int(input("Enter length of side c: "))

if length1==length2==length3:
    print("The triangle is an equilateral.")
elif length1!=length2 and length2!=length3 and length3!=length1:
    print("The triangle is a scalene.")
elif length1==length2 or length2==length3 or length1==length3:
    print("The triangle is an isosceles.")