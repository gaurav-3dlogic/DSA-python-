counter = 1


def printer(name):
    global counter
    if counter <= 10:
        print(name)
        counter += 1
        printer(name)
        
printer("Gaurav")