# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        result, level = 0, [root]
        while root and level:
            result = level[0].val
            level = [child for node in level for child in (node.left, node.right) if child]
        return result
