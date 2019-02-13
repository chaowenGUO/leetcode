# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        level = [root]
        while level:
            result = [node.val if node else None for node in level]
            if result != result[::-1]: return False
            level = [child for node in level if node for child in (node.left, node.right)]
        return True
