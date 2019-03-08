# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        elif not root.left and not root.right and sum == root.val: return [[root.val]]
        else: return [[root.val] + _ for _ in itertools.chain(*map(self.pathSum, (root.left, root.right), (sum - root.val,) * 2))]
