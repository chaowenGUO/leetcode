# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, s):
        if not root: return 0
        elif not root.left and not root.right: return root.val + s * 10
        else: return sum(map(self.dfs, (root.left, root.right), (root.val + s * 10,) * 2))
        
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
