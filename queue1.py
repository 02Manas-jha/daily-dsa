"""
Implement a queue using two stacks


Two approaches 1 of them is via making
push operation expensive
enQueue(q, x): 
While stack1 is not empty, push everything from stack1 to stack2.
Push x to stack1 (assuming size of stacks is unlimited).
Push everything back to stack1.
Here time complexity will be O(n)

deQueue(q): 
If stack1 is empty then error
Pop an item from stack1 and return it
Here time complexity will be O(1)
"""
#Approach 1 Time - O(N+1)
#Space - O(N)
class Queue1:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self,x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    
    def deQueue(self):

        if len(self.s1) == 0:
            return -1
        
        x = self.s1[-1]
        self.s1.pop()

        return x

"""
Approach 2



"""


if __name__ == '__main__':
    q = Queue1()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())