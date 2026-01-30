#print multiplication table of number n giver by user
#by using while loop
n=int(input("enter number "))
i=1
while i<=10:
    print(n*i)
    i+=1

#print square of 1 to 10
n=1
while n<=10:
    print(n**2)
    n+=1

#search for number x in the tuple using loop
#(1,4,9,16,25,36,49,64,81,100)
nums=(1,4,9,16,25,36,49,64,81,100)
x=49
idx=0
while idx<len(nums):
    if(nums[idx]==x):
        print("found at index ",idx)
        idx+=1
        break
else:
    print("finding...")

#print the elements of the following list using a loop
#(1,4,9,16,25,36,49,64,81,100)
#using for
nums=(1,4,9,16,25,36,49,64,81,100)
for el in nums:
    print(el)

#search for a number x in this tuple using for loop
#(1,4,9,16,25,36,49,64,81,100)
nums=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
for el in nums:
    if(nums[i]==x):
        print("found at index ",i)
        i+=1
else:
    print("finding...")

#print multiplication table of number n 
n=int(input("enter number "))
for i in range(1,11):
    print(n*i)

#wap to find the sum of first n numbers(using while)
n=int(input("enter number :"))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print("total sum ",sum)

#Wap to find the sum of first n numbers(using for)
n=int(input("enter number :"))
sum=0
for i in range(1,n+1):
    sum+=i
print("total sum :",sum)

#wap to find the factorial of first n numbers(using while)
n=int(input("enter number"))
i=1
fac=1
while i<=n:
    fac*=i
    i+=1
print("factorial :",fac)

#wap to find the factorial of first n numbers(using for)
n=int(input("enter number :"))
fac=1
for i in range(1,n+1):
    fac*=i
print("factorial :",fac)