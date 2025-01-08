# Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

# Note: If the second largest element does not exist, return -1.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.


# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.


# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 there is no second largest element.

#time - O(n*logn)
def bruteforce(arr):
    n = len(arr)
    arr.sort()
    for i in range(n-2,-1,-1):
        if arr[n-1] != arr[i]:
            return arr[i]
    return -1
#time - O(n)
def optimalsoln(arr):
    largest = -1
    seclargest = -1
    n = len(arr)
    for i in range(n):
        if arr[i] > largest:
            seclargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > seclargest:
            seclargest = arr[i]
    return seclargest

arr = list(map(int,input().split()))
print(optimalsoln(arr))