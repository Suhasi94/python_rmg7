




"""
count = 0
def outer(func):
    def wrapper(*args,**kwargs):
        global count
        print(f"executing {func.__name__} function")
        count += 1
        func(*args,**kwargs) #func = add     
    return wrapper   
#add = wrapper , func = add
@outer
def add(a,b):
    print(a+b)

add(1,2)
add(4,5)
@outer
def sub(a,b):
    print(a-b)
sub(4,6)
print(count)

"""
### create a dictionary to count the number of function calls from each func
"""
d = {}
def outer(func):
    def wrapper(*args,**kwargs):
        print(f"executing {func.__name__} function")
        if func.__name__ not in d:
            d[func.__name__] = 1
        else:
            d[func.__name__] += 1
       
        func(*args,**kwargs) #func = add     
    return wrapper   
@outer #add = outer(add) add = wrapper , func = add
def add(a,b):
    print(a+b)
add(1,2)
add(4,5)
@outer
def sub(a,b):
    print(a-b)
sub(4,6)
print(d)



def outer(func):
    def wrapper(*args,**kwargs):
        print("i m parameterized deco")
        func(*args,**kwargs) #func = add
    return wrapper
def extra(func1):
    def inner(*args,**kwargs):
        print("i m extra deco")
        func1(*args,**kwargs)
    return inner


@outer
@extra #add = paramter(add) add = wrapper , func = add
def add(a,b):
    print(a+b)
add(1,2)

"""
"""

def log(func):
    def wrapper(*args,**kwargs):
        print("i m logging")
        func(*args,**kwargs)
    return wrapper

def register(func1):
    def inner(*args,**kwargs):
        print("i m registered")
        func1(*args,**kwargs)
    return inner

@log
@register 
def main(name,pwd):
    print(name,pwd)
main("suhasini",12345)

"""

"""
def param(n):
    def outer(func):
        def wrapper(*args,**kwargs):
            print(f"executing {func.__name__} function")
            for i in range(n):
                res = func(*args,**kwargs) #func = add
            
        return wrapper 
    return outer
@param(3) #add = outer(add) add = wrapper , func = add
def add(a,b):
    return (a+b)
print(add(1,2))
"""






























