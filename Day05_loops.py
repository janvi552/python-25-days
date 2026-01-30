#loops(while)
count=1 #iteration
while count<=5:
    print(count)
    count+=1

i=5
while i>=1:
    print(i)
    i-=1
print("loop ended")

#print number from 100 to 1
n=100
while n>=1:
    print(i)
    n-=1

#break
nums=(1,2,3,4,5,6,7,8)
while nums<=5:
    if(nums==3):
        nums+=1
        break
    print(nums)
    nums+=1

#continue
a=1
while a<=10:
    if(a%2==0):
       a+=1
       continue
    print(a)
    a+=1

#loops(for)
q=[1,2,3,4,5] 
v=(1,2,3,4,5,6,7,8,9)
str="pythonlearning"
for el in q:
    print(el)
for tuple in v:
    print(tuple)
for char in str:
    print(char)

name="janvi"   
for ele in name:
    print(ele)
else:
    print("END")

t="learning python"
for chr in t:
    if(chr==n):
        print("n found")
    print(chr)
else:
    print("END")

#range
for i in range(10):
    print(i)
for i in range(1,5,2):
    print(i)
for i in range(2,5):
    print(i)

#print 1 to 100
for i in range(1,101,1):
    print(i)

#print 100 to 1
for i in range(100,0,-1):
    print(i)

#pass statement
for el in range(5):
    pass
print("some useful work")

