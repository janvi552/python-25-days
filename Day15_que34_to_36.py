#write a python program for array rotation

def rotate_array(arr,d):
    n=len(arr)

    if d < 0 and d >= n:
        print("invaild input")

    rotated_arr=[0]*n
    for i in range(n):
        rotated_arr[i] = arr[(i +d) % n]

    return rotated_arr

array= [1,2,3,4,5]
d=2
result=rotate_array(array,d)
print(f"orignal array = {array}")
print(f"rotated array = {result}")


#write a python program to split the array and add the first part to the end

def split_and_add(arr,d):
    if d < 0 and d >= len(arr):
        return arr
    
    first_part = arr[:d]
    second_part = arr[d:]

    final = second_part + first_part

    return final

array=[1,2,3,4,5,6,7]
d=4
print(f"orignal array = {array}")
print(f"split the array and add fist part to the end = {split_and_add(array,d)}")


#write a python program to check if given array is monotonic

def is_monotonic(arr):
    increasing=decreasing=True

    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            decreasing = False
        elif arr[i] < arr[i-1]:
            increasing = False

    return increasing or decreasing

arr1=[1,2,3,4,5]
arr2=[4,5,7,2]
arr3=[6,4,3,1]

print(f"arr1 is monotonic : {is_monotonic(arr1)}")
print(f"arr2 is monotonic : {is_monotonic(arr2)}")
print(f"arr3 is monotonic : {is_monotonic(arr3)}")






