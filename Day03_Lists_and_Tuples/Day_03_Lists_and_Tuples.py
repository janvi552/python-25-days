#lists
marks=[94.4,67.8,89.4,77.8,73.9]
print(marks)
print(type(marks))
print(len(marks))
print(marks[1])

student=["karan",18,97,"delhi"]
print(student)
student[0]="yuvi"
print(student)

#list slicing
nums=[7,4,3,1]
nums[1:3]
nums[-3:-1]

#list methods
list1=[2,1,3]
list1.append(4)
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

list2=['b','a','c','d','a']
list2.reverse()
print(list2)

list3=[2,1,5]
list3.insert(1,6)
print(list3)

list4=[2,5,1,2,3]
list4.pop(3)
list4.remove(5)
print(list4)

#tuples
tup=(2,1,4,3)
print(type(tup))
print(tup[0]) 
print(tup[1:3])
print(tup[-3:-1])

#tuple methods
tup=(2,1,3,4,1)
print(tup.index(4))
print(tup.count(1))
