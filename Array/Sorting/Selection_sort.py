def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
           if arr[min_index] > arr[j]: 
            min_index = j
        arr[i] , arr[min_index]= arr[min_index] , arr[i]
    return arr


arr = [70,60,50,40,30,20,10]
result = selectionSort(arr)
print("Sorted Arr after Selection sort ",result)

#time complexity will be  = total comparison + total swap
#                            O(n^2)