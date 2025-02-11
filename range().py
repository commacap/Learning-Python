for i in range(0,10):
    print(i)
print("Introducing a stepover:")
for i in range(0,10,2):
    print(i)
print("Now doing it in reverse")
for i in range(10,1,-1):
    print(i) #only complete if the -1 step is in place, it won't print otherwise