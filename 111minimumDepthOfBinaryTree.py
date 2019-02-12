# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        else:
            *depth, = map(self.minDepth, (root.left, root.right))
            return 1 + (min(depth) or max(depth))
