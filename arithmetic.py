#Create a program that reads two integers, a and b, from the user. Your program should
#compute and display:
#• The sum of a and b
#• The difference when b is subtracted from a
#• The product of a and b
#• The quotient when a is divided by b
#• The remainder when a is divided by b
#• The result of log10 a
#• The result of a^b

import math

a=int(input("Enter first integer: "))
b=int(input("Enter second integer: "))

Sum=a+b
print("Sum:",Sum)

Diff=a-b
print("Difference when b is subtracted from a :",Diff)

Product=a*b
print("Product:",Product)

Quotient=round(a/b,2)
print("Quotient: ",Quotient)

Remainder=a%b
print("Remainder: ",Remainder)

Result=math.log(a,10)
print("Result of log10a:",Result)

last=a**b
print("a^b is:",last)

