"""
Question : detect a cycle on a linked list
Example 1:

Input Format:

LL: 1 2 3 4 5

Result: True

Explanation: The last node with the value of 5 has its 'next' pointer pointing back to a previous node with the value of 3. 
This has resulted in a loop, hence we return true.

Example 2:

Input Format:

LL: 1 2 3 4 9 9

Result: False

Explanation: : In this example, the linked list does not have a loop hence returns false.
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def bruteforce(head):
    temp = head
    hash_set = set()

    while temp is not None:
        if temp in hash_set:
            return True
        
        hash_set.add(temp)
        temp = temp.next
    return False

def optimal(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    fifth.next = third

    print(optimal(head))
