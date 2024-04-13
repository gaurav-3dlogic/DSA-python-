class test:
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        y = self.x
        self.x += 1
        return y
    

p1 = test()
res = iter(p1)

print(next(res))
print(next(res))
print(next(res))