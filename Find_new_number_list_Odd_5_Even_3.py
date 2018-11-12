
evens = []
odds = []

for i in range(1, 200):
    if(i%2==0) and (i%3==0):
        evens.append(str(i))
    elif (i%5==0):
        odds.append(str(i))

print("Result: {}" .format(evens+odds))
