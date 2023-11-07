
# finding sum of elements in an array using divide and conquer

def sum_divide_conquer(array):
    if len(array)==0:
        return 0
    elif len(array)==1:
        return array[0]
    else:
        mid=len(array)//2
        left_array_sum=sum_divide_conquer(array[:mid])
        right_array_sum=sum_divide_conquer(array[mid:])
        return left_array_sum + right_array_sum
    

arr=[4,6,3,7,5,6,8,3,2]
sum=sum_divide_conquer(arr)
print("Sum is:",sum)