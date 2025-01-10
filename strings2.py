"""
Find non repeating character
Examples:

Example 1:
Input: string = “google”
Output: l,e
Explanation: Non repeating characters are l,e.

Example 2:
Input: string = “yahoo”
Output: y,a,h
Explanation: Non repeating characters are y,a,h
"""

def soln(string):
    freq = {}
    for char in string:
        freq[char] = freq.get(char, 0) + 1
    for i, char in enumerate(string):
        if freq[char] == 1:
            print(char, end="")
    return
#time - O(n)
inp = input()
print(soln(inp))