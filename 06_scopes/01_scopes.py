# username = "chaiOrcode"

# def func():
#     # username = "chai"
#     print(username)

# print(username)
# func()
    




# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)


# def func3():
#     global x  # avooide kr na chiya isko 
#     x = 88

# func3()
# print(x)

x = 99
def f1():
    x = 88
    def f2():
        print(x)
    return f2
result = f1()
result()


def chai(num):
    def actual(x):
        return x ** num
    return actual



f = chai(2)
g = chai(3)

print(f(3))
print(g(3))