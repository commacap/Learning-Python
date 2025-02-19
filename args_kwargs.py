#*args and **kwargs
def this_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(this_func(1,2,3,7,15, num1=12, num2=40))