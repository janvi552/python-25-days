#escape sequence charcters
str1="this is a string. \nwe are creating it in python."
str2="this is a string. \twe are creating it in python."
print(str1)
print(str2)

#indexing
str="python learning"
print(str[0])
print(str[8])
#slicing
print(str[1:4])
print(str[5:len(str)])
print(str[:12])
print(str[-3:-1])

#function
str="i am studying python from college"
print(str.endswith("app"))
print(str.capitalize())
print(str.replace("python","java"))
print(str.find("from"))
print(str.count("college"))
print(str.count("o"))

#conditional statements
#
light="green"
if(light=="green"):
    print("go")
elif(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
else:
    print("light was broken")
##
marks=int(input("enter your marks "))
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print("grade of the student =>",grade)

#nesting
age=95
if(age>=18):
    if(age>=80):
        print("cannot drive")
    print("can drive")
else:
    print("cannot drive")


