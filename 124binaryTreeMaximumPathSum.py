# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root):
        left = right = [0, root.val]
        if root.left:
            left = self.dfs(root.left)
            left[0] = max(0, left[0])
        if root.right:
            right = self.dfs(root.right)
            right[0] = max(0, right[0])
        return [root.val + max(left[0], right[0]), max(root.val + left[0] + right[0], left[1], right[1])]
    
    def maxPathSum(self, root: TreeNode) -> int:
        return self.dfs(root)[1]
