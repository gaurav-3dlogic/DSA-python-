def main(func):
    def inner():
        func()
        print("inner")
    return inner

#test



# @main
# def test():
#     print("Testing")
# test()
