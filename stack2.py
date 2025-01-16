"""
Check for balanced paranthesis

Given a string s representing an expression containing various types of brackets: {}, (), and [], the task is to determine whether the brackets in the expression are balanced or not. A balanced expression is one where every opening bracket has a corresponding closing bracket in the correct order.

Example: 

Input: s = “[{()}]”
Output: true
Explanation:  All the brackets are well-formed.


Input: s = “[()()]{}”
Output: true
Explanation: All the brackets are well-formed.


Input: s = “([]”
Output: false
Explanation: The expression is not balanced as there is a missing ‘)’ at the end.


Input:  s = “([{]})”
Output: false
Explanation: The expression is not balanced because there is a closing ‘]’ before the closing ‘}’.



"""

def solution(s):
    stack = []
    mapp = {')':'(',']':'[','}':'{'}

    for char in s:
        if char in mapp:
            top = stack.pop() if stack else '#'
            if mapp[char] != top:
                return False
        else:
            stack.append(char)
    return True

string=input()
print(solution(string))