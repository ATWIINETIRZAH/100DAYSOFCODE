#Write a program that reads a positive integer,n,from the user and then displays thesum of all of the integers from 1 to n
#Thesum of the ﬁrstpositive integers can becomputed using the formula:sum=((n)(n+1))/2

n=int(input("Please enter an integer: "))

if n<0:
    n=int(input("Please enter an integer: "))

Sum=(n*(n+1))/2
print("The sum of integers from 1 to",n,"is: ",Sum)


