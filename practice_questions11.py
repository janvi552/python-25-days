#complex number's sum

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(f"{self.real}i +{self.img}j")

    def __add__(self,num2):
        newreal= self.real + num2.real
        newimg= self.img + num2.img
        return Complex(newreal,newimg)
num1=Complex(4,3)
num1.shownumber()
num2=Complex(7,9)
num2.shownumber()
num3=num1+num2
num3.shownumber()


#define a circle class with radius and define area() & parameter() as a methods of a class

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print(22/7*self.radius**2)

    def parameter(self):
        print(2*22/7*self.radius)

C1=Circle(21)
C1.area()
C1.parameter()


#define a employee class with attribute role,department & salary this class showsdetails() method

class Employee:
    def __init__(self,role,dprt,salary):
        self.role=role
        self.dprt=dprt
        self.salary=salary

    def showdetails(self):
        print(f"role = {self.role}")
        print(f"department = {self.dprt}")
        print(f"salary = {self.salary}")

E1= Employee("accountant","fianace",60000)
E1.showdetails()


#create an engineer class with inheribits properties from employee & has additional attribute: name & age

class Employee:
    def __init__(self,role,dprt,salary):
        self.role=role
        self.dprt=dprt
        self.salary=salary

    def showdetails(self):
        print(f"role = {self.role}")
        print(f"department = {self.dprt}")
        print(f"salary = {self.salary}")

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","software","300000")

Engg1=Engineer("raj",23)
Engg1.showdetails()


#create a class called order which stores item & its price used function __gt__() to convey that :order 1>order2 if price of order 1>price of order2

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price > odr2.price
    
odr1=Order("soap",40)
odr2=Order("pen",15)
print(odr1 > odr2)
    

