#we identify duplicates within a list using python
my_list = ['a','b','c','b','d','m','n','n']

duplicates = []
for letter in my_list:
    if my_list.count(letter) > 1:
        if letter not in duplicates:
         duplicates.append(letter)

print(duplicates)

'''
This exercise was particularly tricky because
I was constrained to use only the knowledge I have
in loops. I also couldn't wrap my head around line 7
but it made sense as I rewrte the code
'''