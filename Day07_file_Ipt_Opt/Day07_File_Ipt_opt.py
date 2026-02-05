#open,read and close file

f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()

#reading a file

f=open("demo.txt","r")
data=f.read(5)
print(data)
f.close()

f=open("demo.txt","r")
line_1=f.readline()
print(line_1)
f.close()

f=open("demo.txt","r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
f.close()

#writing a program

f=open("demo.txt","w")
f.write("i want to learn dsa.")
f.close()

f=open("demo.txt","a")
f.write("then i will move to reactJS")
f.close()

f=open("demo.txt","r+")
f.write("abc")#it prints there curser is
print(f.read())
f.close()

f=open("demo.txt","w+")
print(f.read())
f.write("abc")
f.close()

#with synax

with open("demo.txt","r") as f:
    data=f.read()
    print(data)
    f.close()

with open("demo.txt","w") as f:
    data=f.write("new data")
    print(data)
    f.close()

#deleting a file ex.sample.txt

import os
os.remove("sample.txt")
