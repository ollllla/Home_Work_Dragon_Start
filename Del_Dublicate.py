l = [4,8,9,4,9,4,6,5]

new_list = []

for i in l:
    if i not in new_list:
        new_list.append(i)


print("Result: {}" .format(new_list))

