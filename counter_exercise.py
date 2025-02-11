#create a counter with a list that contains the values from 1-10.
#Sum up all the values in the list.
my_list = list(range(1,11)) #I create a list from a range

counter = 0
for x in my_list:
    counter = counter + x
print(counter)