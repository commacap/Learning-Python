def addition(num1,num2):
    def func2(n1,n2):
        return n1+n2
    return func2(num1,num2)

total = addition(10,20)
print(total)