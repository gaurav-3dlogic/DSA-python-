class abc():
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def test(self):
        print(self.name,self.age)
class xyz(abc):
    pass
p1 = xyz("Gaurav",26)
p1.test()