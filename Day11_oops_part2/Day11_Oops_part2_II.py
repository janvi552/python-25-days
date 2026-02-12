# super method

class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started...")
class Toyotacar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()
car1=Toyotacar("fortuner","electric")
print(car1.name)
print(car1.type)


#class method

class Person:
    name="tarun"

    def changename(self,name):
        self.__class__.name="rahul kumar"

c1=Person()
c1.changename("rahul")
print(c1.name)
print(Person.name)


class Person:
    name="yash"

    @classmethod
    def changename(cls,name):
        cls.name="janvi"
p1=Person()
p1.changename("rahul kumar")
print(p1.name)
print(Person.name)    


#property

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percantage=str((self.phy + self.chem + self.math)/3) +"%"
    
S1=Student(98,97,96)
print(S1.percantage)
S1.phy=90
print(S1.percantage) #error


class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def percantage(self):
        return str((self.phy + self.chem +self.math)/3) + "%"
S1=Student(98,99,92)
print(S1.percantage)
S1.phy=77
print(S1.percantage)


#polymorphism

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(f"{self.real}i + {self.img}j")

num1=Complex(3,4)
num2=Complex(7,11)
num1.shownumber()
num2.shownumber()

