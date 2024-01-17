def decor(printer):
    def inner():
        printer()
        print("Welcome")
    return inner




def printer():
    print("Welcome")
    print("Welcome")
pri = decor(printer)
pri()


#Another Way --


# def decor(printer):
#     def inner():
#         printer()
#         print("Welcome")
#     return inner



# @decor
# def printer():
#     print("Welcome")
#     print("Welcome")
# printer()