#use filter() to extract parts of an iterable
my_list = [1,2,3,4,5]
def find_odds(items):
    return items % 2 != 0

print(list(filter(find_odds, my_list)))