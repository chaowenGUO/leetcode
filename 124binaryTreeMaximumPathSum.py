# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root): # returns: max one side path sum, max path sum
        left = right = [0, root.val]
        if root.left:
            left = self.dfs(root.left)
            left[0] = max(left[0], 0)
        if root.right:
            right = self.dfs(root.right)
            right[0] = max(right[0], 0)
        return [root.val + max(left[0], right[0]), max(root.val + left[0] + right[0], left[1], right[1])]
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)[1]
