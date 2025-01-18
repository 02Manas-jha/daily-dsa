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

enQueue(q,  x)
  1) Push x to stack1 (assuming size of stacks is unlimited).
Here time complexity will be O(1)

deQueue(q)
  1) If both stacks are empty then error.
  2) If stack2 is empty
       While stack1 is not empty, push everything from stack1 to stack2.
  3) Pop the element from stack2 and return it.
Here time complexity will be O(n)

"""
#Time - O(N+1)
#space - O(N)
class Queue2:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self,x):
        self.s1.append(x)
    
    def deQueue(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            return -1
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
        else:
            return self.s2.pop()


if __name__ == '__main__':
    q = Queue1()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())

    q2 = Queue2()
    q2.enQueue(1)
    q2.enQueue(2)
    q2.enQueue(3)

    print(q2.deQueue())
    print(q2.deQueue())
    print(q2.deQueue())