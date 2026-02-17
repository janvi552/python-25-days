#write a python program to calculate the nautral logarithm of any number

import math
num=float(input("enter number : "))
if num <=0:
    print("please enter positive number ")
else:
    print("the nautral logarithm value of ",num ,"is",math.log(num))


#write a python program for cube sum of sum of first n nautral numbers

def cube_sum(n):
    if n<=0:
        print("please enter the positive number ")
    else:
        return sum([i**3 for i in range(1,n+1)])
    
num=int(input("enter the value of n :"))

if num <=0:
    print("enter the vaild input")
else:
    print("the cube of sum of the first",num ,"is",cube_sum(num))


#write a python program to find the sum of array

arr=[1,2,3,4,5]
sum=sum(arr)
print("the total sum of array is",sum)

#or

def sum_of_array(arr):
    total=0
    for ele in arr:
        total+=ele
    return total

array=[1,2,3,4,5]
sum_arr=sum_of_array(array)
print("the total sum of array is",sum_arr)


#write a python program to find largest element in array

def find_largest_element(arr):
    if not arr:
        return "array is empty"
    
    largest_element=arr[0]
    for ele in arr:
        if ele > largest_element:
            largest_element = ele
    return largest_element
array=[24,54,78,90]
result=find_largest_element(array)
print("the largest element in array is ",result)


