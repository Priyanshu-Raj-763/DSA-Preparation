"""
Compute and return the square root of x, where x is guaranteed to be a non-negative
 integer. And since the return type is an integer, the decimal digits are truncated and only
 the integer part of the result is returned. Also, talk about the time complexity of your
 code.
 Test Cases:
 Input: 4
 Output: 2
 Input: 8
 Output: 2
 Explanation: The square root of 8 is 2.8284…., the decimal part is truncated and 2 is
 returned.
 Hint: Try to use a modified binary search approach for an optimized solution
 """
def sqrt(n):
    left  = 0
    right = n
    while left <=right:
        mid = left + (right-left)//2
        curr_sqrt = mid * mid
        if curr_sqrt == n:
            # print("inside if")
            return mid
        elif curr_sqrt > n:
            # print("inside elif")
            right = mid-1
        else:
            # print("inside else")
            left = mid+1

    return right


def decimal_sqrt(n,temp,precision = 4):
    factor = 1
    ans = temp
    for i in range(precision):
        factor = factor /10
        while (ans + factor) * (ans + factor) < n:
            ans = ans + factor
    return ans

        


number  = 8
result = sqrt(number)
res = decimal_sqrt(number,result)
print(f"square root of {number} is ",result)
print(f"decimal square root of {number} is ",res)