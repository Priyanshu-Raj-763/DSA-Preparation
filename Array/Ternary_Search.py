def ternarySearch(arr,i,j,target):
    if(i > j):
        return -1
    
    mid1 = i + (j-i)//3
    mid2 = j -(j-i)//3

    if arr[mid1] == target :
        return mid1
    elif arr[mid2] == target:
        return mid2 
    
    # we are searching on 1st part
    elif target < arr[mid1] :
        return ternarySearch(arr,i,mid1-1,target)
    # we are searching on 3rd part
    elif target >  arr[mid2]:
         return ternarySearch(arr,mid2+1,j,target)
    # we are searching on 2nd part
    else:
         return ternarySearch(arr,mid1 +1,mid2-1,target)
    


arr = [20,25,32,35,39,41,42,49,51,60]
result = ternarySearch(arr,0,len(arr)-1,55)
print("the value is present at index no ",result)