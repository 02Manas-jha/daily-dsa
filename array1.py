# Given an array arr[], the task is to find the subarray that has the maximum sum and return its sum.

# Examples:

# Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
# Output: 11
# Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.


# Input: arr[] = {-2, -4}
# Output: –2
# Explanation: The subarray {-2} has the largest sum -2.


# Input: arr[] = {5, 4, 1, 7, 8}
# Output: 25
# Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.

#time - O(n^3)
def bruteforce(arr, n):
    maxi = float("-inf")
    for i in range(n):
        for j in range(i,n):
            sumSub = 0
            for k in range(i, j+1):
                sumSub += arr[k]
            maxi = max(maxi, sumSub)
    return maxi
#time - O(n^2)
def bettersoln(arr,n):
    maxi = float("-inf")
    for i in range(n):
        sumSub = 0
        for j in range(i, n):
            sumSub += arr[j]
            maxi = max(maxi, sumSub)
    return maxi
#time - O(n)
def optimalsoln(arr, n):
    max_sum = arr[0]
    curr_sum = arr[0]
    for i in range(1, n):
        curr_sum = max(arr[i], curr_sum+arr[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum

n = int(input())
arr = list(map(int,input().split()))
print(optimalsoln(arr,n))