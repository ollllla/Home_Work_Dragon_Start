import random

lst = random.sample(range(1,100), 15)
print("Input list: {}" .format(lst))

def sorting_list(i):
    return i[:]

order = sorting_list(lst)
order.sort()
if lst == order:
    print ('Given list is SORTED.')
else:
    print ('List NOT Sorted.')
