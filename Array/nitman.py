
#12.57min video se phle k notes bhi banane h


#__init function
#Defination - constructor are used to initialize the objects state

class person:
    def __init__(self,name):
        self.name = name
    
    def say_hi(self):
        print(f"Hello my name is {self.name}")

p = person('Gaurav')
p.say_hi()


#ternary
#expression = [if_true] if [expression] else [if_false]
age = 25
discount = 20 if age > 18 else 10
print(discount)


#inheritance  def - child class can all inherit the properties and behaviour from parents class
class A:
    def __init__(self):
        print("A display")

class B(A):
    def show(self):
        print("B display")
res = B()
res.show()
