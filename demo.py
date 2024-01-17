def decor(printer):
    def inner():
        printer()
        print("First function call")
    return inner




def printer():
    print("Hey this decorator")

pri = decor(printer)
pri()