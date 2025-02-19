my_list = [1,2,-3,-4,5,-6,7,-8,10]

multiplyby2= [x*2 for x in my_list]
print(multiplyby2)

positives = [y for y in my_list if y > 0]
print(positives)

evens = [z for z in my_list if z % 2 == 0]
print(evens)

odds = [z for z in my_list if z % 2 != 0]
print(odds)