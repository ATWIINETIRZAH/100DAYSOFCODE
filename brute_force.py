

list=[4,6,32,7,832,4,9,3,7,3,9]

inv=0

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            inv=inv+1

print("Number of inversions:",inv)