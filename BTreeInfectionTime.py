# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given a binary tree and a start node, find the longest path to another node.

# Idea: traverse the tree postorder. Pass the longest of child paths until start node is found. Pass negative values to denote when the start node has been found.
# When a node has a child that has found the start node (negative), it must pass the value subtracted by one after testing the path going through the node.

class Solution(object):
    top = 0
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        if not root: return 0
        l = self.recur(root.left, start)
        r = self.recur(root.right, start)

        return max(l, r) if start == root.val else max(abs(l) + abs(r), self.top)

    def recur(self, root, start):
        if not root: return 0
        l = self.recur(root.left, start)
        r = self.recur(root.right, start)

        if root.val == start:
            self.top = max(l, r)
            return -1
        else:
            a, b = l<0, r<0
            if a or b: self.top = max(self.top, abs(l) + abs(r))
            if a: return l - 1
            elif b: return r - 1
            return max(l, r)+1