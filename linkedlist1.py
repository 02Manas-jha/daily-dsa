"""
Question: Reverse a singly Linked List
i/p: 1->2->3->4->5->none
o/p: 5->4->3->2->1->none
"""



class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def bruteforce(head):
    temp = head
    stack = []
    while temp is not None:
        stack.append(temp.data)
        temp = temp.next
    temp = head
    while temp is not None:
        temp.data = stack.pop()
        temp = temp.next
    return head
#Time - O(N)
#Space - O(N)

def optimalsoln(head):
    prev = None
    curr = head

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
#Time - O(N)
#Space - O(1)

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original Linked List:", end=" ")
print_linked_list(head)

head = optimalsoln(head)

print("Reversed Linked List:", end=" ")
print_linked_list(head)