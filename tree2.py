"""Binary search tree"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def search(root,x):

    if root is None or root.val == x:
        return root.val
    
    if root.val<x:
        return search(root.right,x)
    return search(root.left,x)

def isBST(node, min, max):
    if node == None:
        return True
    
    if node.val <= min or node.val >= max:
        return False
    
    return isBST(node.left, min, node.val) and isBST(node.right, node.val, max)

root = Node(9)
root.left = Node(1)
root.right = Node(10)
root.left.left = Node(0)
root.left.right = Node(3)
root.left.right.right = Node(4)

mini = 0
maxi = 10
print(isBST(root, mini, maxi))