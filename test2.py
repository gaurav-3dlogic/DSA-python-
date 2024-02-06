counter = 1

c = 0




def printer(name):
   
    global counter,c
    if counter <= 10:
        c += 1
        print(name)
      
        counter += 1

        printer(name)

printer(counter)
print(c)
