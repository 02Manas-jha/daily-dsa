"""
Given a postfix expression, the task is to evaluate the postfix expression. A Postfix expression is of the form “a b operator” (ab+) i.e., a pair of operands is followed by an operator.

Examples:

Input: str = “2 3 1 * + 9 -“
Output: -4
Explanation: If the expression is converted into an infix expression, it will be 2 + (3 * 1) – 9 = 5 – 9 = -4.


Input: str = “100 200 + 2 / 5 * 7 +”
Output: 757
"""
#Time - O(N)
#space - O(N)
class Stack:

    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity

        self.arr = []

    def isEmpty(self):
        return True if self.top == -1 else False
    
    def peek(self):
        return self.arr[-1]
    
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.arr.pop()
        else:
            return "$"
    
    def push(self,op):
        self.top += 1
        self.arr.append(op)
    
    def solution(self, exp):
        for i in exp:

            if i.isdigit():
                self.push(i)
            
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2+i+val1)))

        return int(self.pop())

if __name__ == "__main__":
    exp = input()
    obj = Stack(len(exp))

    print(obj.solution(exp))

