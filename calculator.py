class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=cal(a,b)
choice=1
print("0. Exit")
print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
while choice!=0:

    choice=int(input("Enter choice: "))
    if choice==1:
        print("Sum of entered numbers is : ",obj.add())
    elif choice==2:
        print("Subtraction of entered numbers is: ",obj.sub())
    elif choice==3:
        print("Multiplication result of numbers is: ",obj.mul())
    elif choice==4:
        print("Division of entered numbers is : ",round(obj.div(),2))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid, Please enter valid choice!!")
 
 
print()