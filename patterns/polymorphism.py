class car:
    def __init__(self,name,model):
        self.name = name 
        self.model = model

    def move(self):
        print("Drive")

class program:
    def __init__(self,name,language):
        self.name = name
        self.language = language    
    
    def move(self):
        print("bug")

class gym:
    def __init__(self,name,exercise):
        self.name = name
        self.exercise = exercise
    def move(self):
        print("lift")

p1 = car("Swift",2022)
p2 = program("python","c")
p3 = gym("dumble","back")

for i in (p1,p2,p3):
    i.move()
