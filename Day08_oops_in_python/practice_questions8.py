#create student class that take name & marks of 3 subjects as aruguments in constructors then create to print the avarage

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your avg score is",sum/3)

s1=Student("karan",[98,97,96])
s1.get_avg()

s1.name="ironman"
s1.get_avg()

#create account class with 2 attribute-balance & account no and create methods for debit,credit & printing the balance

class Account:
    def __init__(self,acc_no,balance):
        self.balance=balance
        self.acc_no=acc_no

    def debit(self,amount):
        self.balance-=amount
        print("rs.",amount,"was debited")
        print("total balance is",self.balance)

    def credit(self,amount):
        self.balance+=amount
        print("rs.",amount,"was credited")
        print("total balance is",self.balance)

    def get_balance(self):
        return self.balance

acc1=Account(12345,10000)
print(acc1.balance)
print(acc1.acc_no)
acc1.debit(500)
acc1.credit(1000)