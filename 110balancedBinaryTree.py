# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, root):
        if not root: return 0
        else:
            left, right = map(self.check, (root.left, root.right))
            if left == -1 or right == -1 or abs(left - right) > 1: return -1
            else: return 1 + max(left, right)
            
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root) != -1
