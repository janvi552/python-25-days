#store in dictionary some random word and their meaning
dictionary ={
    "table":["a piece of furniture","list of facts & figures"],
    "cat":"a small animal"
}
print(dictionary)

#how many classroom needed for each language
list={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(list))

#3 subject from the user and store in dictionary
marks={}
x=int(input("enter phy marks "))
marks.update({"phy": x})
x=int(input("enter chem marks "))
marks.update({"chem": x})
x=int(input("enter maths marks "))
marks.update({"maths": x})
print(marks)

#one same int & float store in the set
values={9,9.0}
print(values)
values={("int",9),("float",9.0)}
print(values)
#or
values={9,"9.0"}
print(values)