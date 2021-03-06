'''
Write a function that takes in a Binary Search Tree (BST) and a target integer value
and returns the closest value to that target value contained in the BST.
You can assume that there will only be one closest value.
Each BST node has an integer value a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property:
its value is strictly greater than the values of every node to its left: its value is less than or equal
to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None null .
'''

# Solution 1
# On Average: O(Log(n)) Time | O(Log(n)) Space
# Worst Case: O(n) Time | O(n) Space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float('Inf'))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(tree.value - target) < abs(target - closest):
        closest = tree.value
    if tree.value < target:
        return findClosestValueInBstHelper(tree.right, target, closest)
    elif tree.value > target:
        return findClosestValueInBstHelper(tree.left, target, closest)
    else:
        return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Solution 2
# On Average: O(Log(n)) Time | O(1) Space
# Worst Case: O(n) Time | O(1) Space

def findClosestValueInBstNew(tree, target):
    return findClosestValueInBstNewHelper(tree, target, float("inf"))

def findClosestValueInBstNewHelper(tree, target, closest):
    current_tree = tree
    while current_tree is not None:
        if abs(current_tree.value - target) < abs(target - closest):
            closest = current_tree.value
        if current_tree.value < target:
            current_tree = current_tree.right
        elif current_tree.value > target:
            current_tree = current_tree.left
        else:
            break
    return closest



# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


