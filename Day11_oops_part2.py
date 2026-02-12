#del keyword

class Student:
    def __init__(self,name):
        self.name=name
s1=Student("karan")
print(s1.name)
del s1
# print(s1.name)   error


#private attribute & methods

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset(self):
        print(self.__acc_pass)
acc1=Account("12345","abcde")
print(acc1.acc_no)
print(acc1.reset())

class person:
    __name="rahul"
    def __hello(self):
        print("hello user!")
    def welcome(self):
        print(self.__hello())
h1=person()
print(h1.welcome())


#inheritance

#single inheritance

class Car:
    colour="black"
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stopped...")

class Toyotacar(Car):
    def __init__(self,name):
        self.name=name

car1=Toyotacar("prius")
car2=Toyotacar("fortuner")
car1.start()
car2.stop()
print(car1.colour)
print(car2.name)

#multi-level inheritance

class Car:
    colour="white"
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stopped...")
    
class Toyotacar(Car):
    def __init__(self,name):
        self.name=name

class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("electric")
car1.start()
print(car1.type)
print(car1.colour)

#multiple-inheritance

class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class C"
C1=C()
print(C1.varA)
print(C1.varB)
print(C1.varC)


#super method

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

