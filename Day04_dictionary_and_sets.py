#dictionary
info={
    "name":"arjun",
    "learning":"coding",
    "age":35,
    "is_adult":True,
    "topics":("dict","set"),
    "subjects":["python","java","c++"]
}
print(info)
print(type(info))
print(info["name"])
print(info["subjects"])
info["name"]="rahul"
info["surname"]="joshi"#to add something
print(info)

#null dictionary
null_dict={}
null_dict["name"]="janvi"
print(null_dict)

#nested dictionary
student={
    "name":"kunal",
    "marks":{
        "phy":98,
        "chem":90,
        "maths":99
    }
}
print(student)
print(student["marks"])
print(student["marks"]["chem"])

#dictionary methods
student={
    "name":"tarun kumar",
    "subjects":{
        "phy":98,
        "chem":90,
        "math":99
    }
}
print(student.keys())
print(list(student.keys()))
print(list(student.values()))
print(len(list(student.keys())))
print(list(student.items()))
pairs=list(student.items())
print(pairs[1])

#print(student("surname")) error
print(student.get("surname"))

student.update({"city":"delhi"})
print(student)

#set
collection={"hello","world","python","coding","learning",4,3,4,2,1}
print(collection)
print(len(collection))
print(type(collection))

#set methods
nums=set() #empty set synax
nums.add(1)
nums.add(2)
nums.add(2)
print(nums)
nums.remove(2)
nums.add((1,2,3)) #tuples allowed
#nums.add([1,2,3]) #list not allowed
print(nums)
nums.clear()
print(len(nums))

#pop
words={"hello","world","python","java","coding"}
print(words.pop())
print(words.pop())

#union-intersection
set1={1,2,4}
set2={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1)
print(set2)





