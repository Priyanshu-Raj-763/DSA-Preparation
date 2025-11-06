
def binarySearch_2d(arr,target):
    row = len(arr)
    col = len(arr[0])
    start  = 0
    end = row*col - 1
    # dhyan dena row and col dono me mid ko col se hi divide and modulo karna hota hai
    while(start <= end):
        mid = start + (end-start)//2
        mid_value = arr[mid//col][mid%col] 
        if(target == mid_value):
            return True
        elif( mid_value > target):
            end = mid -1
        else:
            start = mid +1
    return False
arr_2d = [[1,3,5,7]
        ,[10,11,16,17]
        ,[23,30,34,60]]
result = binarySearch_2d(arr_2d,43)
print("Target = ",result)

