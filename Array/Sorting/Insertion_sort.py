def insertionSort(arr):
    n = len(arr)
    for i in range (1,n) :
        j = i-1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j+1]  = arr[j]
            j-=1
        arr[j+1] = key
    return arr
arr = [70,60,50,40,30,20,10]
result = insertionSort(arr)
print("Sorted Arr after insertion sort ",result)

#Time complexity = O(n^2)