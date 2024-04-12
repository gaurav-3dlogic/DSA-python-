
def test(n):
    return lambda x: x * n
res = test(5)
print(res(6))