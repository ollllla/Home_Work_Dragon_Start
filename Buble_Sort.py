list = [64, 34, 25, 12, 22, 11, 90, 15, 17, 5, 8]

def bubbleSort(list):
    n = len(list)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater
            # than the next element
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]

bubbleSort(list)

print("Result: {}" .format(list))
