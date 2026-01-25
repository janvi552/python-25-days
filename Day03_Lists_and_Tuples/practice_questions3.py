#ask the user to enter their 3 fav movies & store them in a list
movies=[]
movies.append(input("enter first movie name :"))
movies.append(input("enter second movie name :"))
movies.append(input("enter third movie name :"))
print(movies)

#check if a list contains a palindrome of elements
list=["b","a","c","a","b"]
list_copy=list.copy()
list.reverse()
if(list==list_copy):
    print("palindrome")
else:
    print("NOT palindrome")

#count the number of students with the "A" grade
tup=("B","C","A","C","A","D")
tup.count("A")
print(tup)

#store the above values in a list & sort them "A" to "D"
list=["B","C","A","C","A","D"]
list.sort()
print(list)