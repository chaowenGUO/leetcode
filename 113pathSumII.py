# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import typing
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> typing.List[typing.List[int]]:
        if not root: return []
        elif not root.left and not root.right and sum == root.val: return [[root.val]]
        else: return [[root.val] + _ for _ in self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)]
