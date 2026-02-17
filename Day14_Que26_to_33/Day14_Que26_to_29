#write a python program to make a simple calculator with 4 basic mathmatical operations

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y

print("choose one upto 1/2/3/4 :")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.division")

while True:
    choice=input("enter the choice upto 1/2/3/4 :")

    if choice in ('1','2','3','4'):
        try:
            num1=int(input("enter first number :"))
            num2=int(input("enter second number :"))
        except ValueError:
            print("invaild input.enter vaild number..")
            continue

        if choice=='1':
            print(f"{num1} + {num2} = {add(num1,num2)}")
        elif choice=='2':
            print(f"{num1} - {num2} = {subtract(num1,num2)}")
        elif choice=='3':
            print(f"{num1} * {num2} = {multiply(num1,num2)}")
        elif choice=='4':
            print(f"{num1} / {num2} = {division(num1,num2)}")

        next_cal=input("let's do next calculation ?? (yes/no)")
        if next_cal=='no':
            break
    else:
        print("invaild input..")


#write a python program to display fibonacci sequence using recursion

def recur_fibo(n):
    if n<=1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))
    
nterms=int(input("how many terms ? (greater than 0) : "))
if nterms <= 0:
    print("iplease enter a positive number ")
else:
    for i in range(nterms):
        print(recur_fibo(i))


#write a python program to find factorial of number using recursion

def recur_fact(n):
    if n == 1:
        return n
    else:
        return n*recur_fact(n-1)
    
num=int(input("enter number (greater than or equal to 0):"))
if num < 0:
    print("invaild input. enter a positive number")
elif num ==0:
    print("the factorial of 0 is 1")
elif num >0:
    print("the factorial of", num ,"is", recur_fact(num))


#write a python program to calculate your body mass index

def bodymassindex(height,weight):
    return round((weight/height**2),2)

print("welcome to the bmi calculator ")

h=float(input("enter your height in meters : "))
w=float(input("enter your weight in kilograms : "))
 
bmi=bodymassindex(h,w)

print("your bmi is ",bmi)

if bmi < 18.5:
    print("you are underweighted")
elif 18.5 <= bmi <= 24.9:
    print("your weight is normal")
elif 25 <= bmi <=29.29:
    print("you are overweighted")
else:
    print("you are obese")


