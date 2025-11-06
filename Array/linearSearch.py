def linearSearch(arr,key):
    for i in range(len(arr)):
        if key == arr[i]:
            return i
    return -1



arr = [34,554,43,88,545,987,34,85,33,88,54,86]
result  = linearSearch(arr,43)

print("the element is present at this index -->",result)