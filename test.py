class abc:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def test(self):
        print(self.name,self.age)

class xyz(abc):
    def __init__(self,name,age,college):
        super().__init__(name,age)
        self.college = "sharda"
   
    def moba(self):
        print(self.name,self.age,self.college,"Hey")

p1 = xyz("Gaurav",27,"sharda")
print(p1.moba())