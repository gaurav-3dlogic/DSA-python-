class abc:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def test(self):
        print(self.name, self.age)
class xyz(abc):
    def __init__(self,name,age):
        super().__init__(name,age)
p1 = xyz("Gaurav",27)
p1.test()


        
