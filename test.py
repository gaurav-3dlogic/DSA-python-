#test new
def decor(printer):
    def inner():
        printer()
        print("inner")
    return inner

@decor
def printer():
    print("test")

printer()


