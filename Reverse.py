def insertionSort(L, reverse=False):
    if reverse:
        cmpfunc = lambda a, b: cmp(b, a)
    else:
        cmpfunc = cmp
    for j in xrange(1,len(L)):
        valToInsert = L[j]
        i=j-1
        while i>=0 and cmpfunc(L[i], valToInsert) > 0:
            L[i+1] = L[i]
            i-=1
        L[i+1] = valToInsert
    return L
