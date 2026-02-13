#write a python program to find the factorial of a Number

num=int(input("enter number : "))
fact=1
if num<0:
    print("factorial does not exist")
elif num==0:
    print("factorial =1")
elif num>0:
    for i in range(1,num+1):
        fact=fact*i
print(f"factorial ={fact}")


#write a python program to display the multiplication table

num=int(input("enter number : "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")


#