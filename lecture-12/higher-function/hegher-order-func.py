def apply_function(func,value):
    return func(value)

def square(x):
    return x*x

def add(x):
    return x+x


print(apply_function(square,5))
print(apply_function(add,5))