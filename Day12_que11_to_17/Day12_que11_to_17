#write a python program to check if a number is positive,negative or Zero

num=float(input("enter number : "))
if num > 0:
    print("POSITIVE")
elif num < 0:
    print("NEGATIVE")
else:
    print("zero")


#write a python program to check if a number is odd or even

num=float(input("enter number : "))
if num%2==0:
    print("EVEN number")
else:
    print("ODD number")


#write a program to check leap year

year=int(input("enter year : "))
if (year%4==0) and (year%100 != 0):
    print(f"{year} is the Leap year") 
elif (year%400==0) and (year%100==0):
    print(f"{year} is the Leap year")
else:
    print(f"{year} is not Leap year")


#write a python to check prime number:

num=int(input("enter a number : "))
flag=False
if num==1:
    print("1 is not a prime number")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            flag=True
            break
if flag:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")


#write a program to print all prime numbers in an interval of 1-10

lower=1
upper=10
print("prime numbers between ",lower,"and",upper,"are :")
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if (num%i == 0):
                break
        else:
            print(num)

