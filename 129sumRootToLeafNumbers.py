# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, s):
        if not root: return 0
        elif not root.left and not root.right: return s * 10 + root.val
        else: return self.dfs(root.left, s * 10 + root.val) + self.dfs(root.right, s * 10 + root.val)
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """      
        return self.dfs(root, 0)
