# LEGB local--->enclosing-->global-->builtin

# 变量的作用域，变量的生命周期
x = 100 #全局

def foo():
    print("foo x", x)

def bar():
    x = 10
    print("bar x", x)

foo()
bar()