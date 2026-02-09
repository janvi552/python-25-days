#oop in python

#class & object

class Student:
    name="arjun"
s1=Student()
print(s1) #object
print(s1.name)
s2=Student()
print(s2.name)

class Car:
    colour="black"
    brand="BMW"
car1=Car()
print(car1.colour)
print(car1.brand)

#__init__ function

class Student:
    name="rahul"
    marks="88"
    def __init__(self):
        print("adding new student in database...")
s1=Student()
print(s1.name)
print(s1.marks)

class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("adding new student in database...")
s1=Student("karan")
print(s1.name)
s2=Student("prince")
print(s2.name)

class Student:
    def __init__(self,name,marks):  #parameterized constructor
        self.name=name
        self.marks=marks
        print("adding new student in database...")
s1=Student("tarun",98)
print(s1.name)
print(s1.marks)
s2=Student("shagun",91)
print(s2.name)
print(s2.marks)

#default constructor

def __init__(self):
    pass

#class & instance atribute

class Student:
    collegename="IIT Madras" #class attr
    name="anonymous"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in database...")

s1=Student("janvi",95) #obj.attr > class.attr
print(s1.name)
print(s1.marks)

#methods

class Student:
    clg_name="IIT Madras"
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
    def welcome(self):
        print("welcome back",self.name)
    def get_marks(self):
        print("you got",self.marks,"marks")
s1=Student("gargi",90)
s1.welcome()
s1.get_marks()

#static methods

class hello:
    @staticmethod   #decorter
    def hello(self):
        print("hello")

#Abstraction

class Car:
    def __init__(self):
        self.clutch=False
        self.acc=False
        self.brk=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started...")

car1=Car() #necessary items show
car1.start()

#encapsulation
'wrapping data & functions into a single object'

