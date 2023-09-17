# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places.
container_size=int(input("please enter the size of container: "))
number_1litre_container=int(input("please enter the number of containers 1 litre and below: "))
number_morethan1litre_container=int(input("please enter the number of containers more than 1 litre: "))
refund1=number_1litre_container*0.10
refund2=number_morethan1litre_container*0.20
total_refund=refund1+refund2
print("The total refund is ${:.2f}".format(total_refund))