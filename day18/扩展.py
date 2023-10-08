# def foo(*x, **kwargs):
#     print(x)
#     print(kwargs)
#
# foo(1,2,3,4,5, name="yuan", age=18)


def bar(x,y,z):
    print(x)
    print(y)
    print(z)

bar(*[1,2,3]) # bar(1,2,3)
