#WAF to print the length of a list(list is the parameter)

def list_length(list):
    print(len(list))
    return
veggies=["tomato","cucumber","ladyfinger"]
list_length(veggies)


#WAF to print the element of a list in a simgle line (list is a parameter)

def list_ele(list):
    for i in list:
        print(i,end=" ")
    return
cities=["chennai","surat","mumbai","delhi","chandigadh"]
list_ele(cities)


#WAF to find the factorial of n(n is a parameter)

def calc_fact(n):
    if(n==0 or n==1):
        return 1
    return calc_fact(n-1)*n
print("factorial :",calc_fact(4))
print("factorial :",calc_fact(5))


#WAF to convert USD to INR

def cvrt(USD):
    INR=USD*83
    print(USD,"$=",INR,"rupees")
    return
cvrt(14)
cvrt(63)


#WAF to find the number is EVEN or ODD

def number(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")
    return
number(345)
number(88)

#write a recursive function to calculate the sum of first n nautral numbers
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n
print(calc_sum(5))
print(calc_sum(10))

#write a recursive function to print all elements in a list 
def list_ele(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    return list_ele(list,idx+1)
heroes=["thor","spiderman","batman","shaktimaan"]
list_ele(heroes)