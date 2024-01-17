



def decor(printer):
    def inner():
        printer()
        print("First welcome")
    return inner



@decor
def printer():
    print("Welcome")

printer()
