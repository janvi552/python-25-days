#que1

print("hello python")

#arithmatic operations
#que2

a=int(input("enter first :"))
b=int(input("enter second :"))
sum=a+b
diff=a-b
print(sum)
print(diff)

#que3
#triangle"s area
base=float(input("enter base's length :"))
height=float(input("enter height's length :"))
area=(height*base)/2
print(area)

#que4
#swape two variables
a=int(input("enter first :"))
b=int(input("enter sec :"))
print(f"origanal values : a = {a}, b = {b} ")
temp=a
a=b
b=temp
print(f"swapped number : a = {a},b = {b}")


#que5
#import random variable
import random
print(f"random number : {random.randint(1,100)}")