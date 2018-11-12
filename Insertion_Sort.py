def insertionSort(list):
   for i in range(1,len(list)):

     k = list[i]
     j = i

     while j>0 and list[j-1] > k:
         list[j]=list[j-1]
         j = j-1

     list[j]=k

list = [54,26,93,17,77,31,44,55,20]
insertionSort(list)
print(list)
