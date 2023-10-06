# LEGB local--->enclosing-->global-->builtin

# 变量的作用域，变量的生命周期
x = 100 #全局

def foo():
    # x = 10
    print("foo...")

    def bar():
        # x = 1
        print("bar x", x)

    bar()

foo()