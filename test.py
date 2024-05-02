
# def decor(printer):
#     def inner():
#         printer()
#         print("inner")
#     return inner
#test
@decor
def printer():
    print("test")

printer()


