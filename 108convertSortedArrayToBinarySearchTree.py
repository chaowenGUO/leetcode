# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import typing
class Solution:
    def sortedArrayToBST(self, nums: typing.List[int]) -> TreeNode:
        if not nums: return None
        else:
            middle = len(nums) // 2
            root = TreeNode(nums[middle])
            root.left = self.sortedArrayToBST(nums[:middle])
            root.right = self.sortedArrayToBST(nums[middle + 1:])
            return root
