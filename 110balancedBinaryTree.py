# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, root: TreeNode) -> int:
        if not root: return 0
        else:
            left, right = map(self.check, (root.left, root.right))
            return -1 if left == -1 or right == -1 or abs(left - right) > 1 else 1 + max(left, right)
            
    def isBalanced(self, root: TreeNode) -> bool:
        return self.check(root) != -1
