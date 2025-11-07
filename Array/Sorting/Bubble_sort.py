def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swapped = True
        if not swapped: # for more optimization if arr no swaps is required then the loop will stop from doing uneccessary comparison
            break
    return arr


arr = [70,60,50,40,30,20,10]
result = bubbleSort(arr)
print("Sorted Arr after bubble sort ",result)

#Time complexity = O(n^2)