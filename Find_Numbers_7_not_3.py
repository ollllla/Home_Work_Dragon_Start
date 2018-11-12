new_list=[]
for i in range(1500, 2701):
    if (i%7==0) and not (i%3==0):
        new_list.append(str(i))
print (','.join(new_list))
