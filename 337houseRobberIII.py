# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root):
        if not root: return (0,) * 2
        else:
            left, right = map(self.dfs, (root.left, root.right))
            return left[1] + right[1], max(left[1] + right[1], root.val + left[0] + right[0])
        
    def rob(self, root: TreeNode) -> int:
        return self.dfs(root)[1]
        
