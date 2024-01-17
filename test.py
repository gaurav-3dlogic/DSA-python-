def decor(printer):
    def inner():
            printer()
            print("Welcome")
    return inner

def printer():
        print("Welcome")
        print("welcome")
pri = decor(printer)
pri()
