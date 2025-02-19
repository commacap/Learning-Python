#reduce applies a function to the first 2 elements of an iterable and reduce it to a single cummulative value
from functools import reduce
my_networth = [1200, 10000, 16000, 50000]
def wealth(source,value):
    return source + value

print(reduce(wealth,my_networth))
#this application of reduce gives me a total of my networth from different sources

my_list = ['W','E','A','L','T','H']
def the_bag(x,y):
    return x + y

print(reduce(the_bag,my_list))
