#Q : u have given a sorted array and u have to find the index of the elements which satify the given condition like (a+b = 180) so have to find the elements whose sum is equal to 180 
#the approach used is two pointer approach

def two_sum (arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        cur_sum = arr[left] + arr[right]
        if cur_sum == target:
            return (left,right)
        elif cur_sum > target:
            right -= 1
        else:
            left += 1
    return(-1,-1)



arr = [20,40,60,80,90,120,240]
target = 210
print("The target is found at index = ",two_sum(arr,target))

