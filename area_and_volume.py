#Write a program that begins by reading a radius, r, from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r. Use the pi constant in the math module in your
# calculations.


import math

r=int(input("Enter radius: "))

Area= math.pi * r*r

Volume= (4/3) * math.pi * r*r

print(f"Volume is: {Volume}")
print(f"Area is {Area}")


