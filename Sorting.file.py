l = [4,8,9,4,9,4,6,5]
print("Input list: {}" .format(l))

for i in range(1, len(l)):
    k = l[i]
    j = i-1
    while j >= 0 and k < l[j]:
        l[j+1]= l[j]
        j -= 1
    l[j+1] = k

items = [l[0]]
count = [1]

for i in range(1, len(l)):
    if l[i] != l[i-1]:
        items.append(l[i])
        count.append(1)
    else:
        count[-1] += 1

for i in range(1, len(count)):
    k = count[i]
    d = items[i]
    j = i-1
    while j >= 0 and k > count[j]:
        count[j+1] = count[j]
        items[j+1] = items[j]
        j -= 1
    count[j+1] = k
    items[j+1] = d

result = []

for i in range(len(count)):
    for j in range(count[i]):
        result.append(items[i])

print("Result: {}" .format(result))

