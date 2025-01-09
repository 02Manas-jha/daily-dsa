"""
Q1. Check if a string is a palindrome

input : "aba"
output : 1

input : "MANAS"
output : 0
"""


def brutesol(string):
    if string[::-1] == string:
        return 1
    return 0

def optimal(string):
    left = 0
    right = len(string) - 1

    while left<right:
        if string[left] != string[right]:
            return 0
        left += 1
        right -= 1
    return 1

s = input()
print(brutesol(s))