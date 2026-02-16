def compute_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    
    while(True):
        if((greater % x==0) and (greater % y==0)):
            lcm=greater
            break
        greater+=1
    return lcm
num1=int(input("enter first number :"))
num2=int(input("enter second number :"))

print("The L.C.M. is",compute_lcm(num1,num2))


#write a python program to find HCF

def compute_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if ((x % i == 0) and (y % i ==0)):
            hcf=i
    return hcf
    
num1=int(input("enter first number :"))
num2=int(input("enter second number :"))

print("the H.C.F is ",compute_hcf(num1,num2))


#write a python program to convert decimal to binary,octal,hexadecimal

dec_num=int(input("enter decimal number :"))

print("the decimal value of ",dec_num,"is :")

print(bin(dec_num),"in a binary")
print(oct(dec_num),"in a octal")
print(hex(dec_num),"is a hexadecimal")


#write a python program to find ASCII value of a character

char =str(input("enter character :"))
print("The ASCII value of '"+char+"' is ",ord(char))