#user's first name &its length
name=input("enter your name ")
print("the length of your name is ",len(name))

#the occurense of '$' in a string
str="hello,$ i am $$ coder & right$ now i am doing $it."
print(str.count("$"))

#number entered by user is odd or even?
num=int(input("enter number "))
if(num%2==0):
    print("number is even.")
else:
    print("number is odd.")

#the greatest number of 3 numbers entered by user
a=int(input("enter first :"))
b=int(input("enter second :"))
c=int(input("enter third :"))
if(a>=b and a>=c):
    print("first is the largest number ",a)
elif(b>=c):
    print("second is the largest number ",b)
else:
    print("third is the largest ",c)

#the given number is multiple of 7 or not?
num=int(input("enter number "))
if(num%7==0):
    print("the number is mutiple of 7")
else:
    print("the number is not multiple of 7")