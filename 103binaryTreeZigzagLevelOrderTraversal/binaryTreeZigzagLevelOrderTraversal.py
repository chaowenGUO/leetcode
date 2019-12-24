# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result, level, direction = [], [root], 1
        while root and level:
            result += [node.val for node in level][::direction],
            direction *= -1
            level = [child for node in level for child in (node.left, node.right) if child]
        return result
