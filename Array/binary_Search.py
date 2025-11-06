def binarySearch(arr,key) :
    start = 0
    end = len(arr) - 1
    while(start <= end):
        mid = end - (end-start)//2
        if(arr[mid] == key):
            # print("mid == key")
            return mid
        elif(arr[mid] > key):
            # print("mid > key")
            end = mid - 1
        elif(arr[mid] < key):
            # print("mid < key")
            start = mid + 1

arr = [12,34,56,66,79,80,96,103,111]
result = binarySearch(arr,34)
print("The given key is present at index = ",result)
