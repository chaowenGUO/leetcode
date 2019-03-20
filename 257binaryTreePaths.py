# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        elif not root.left and not root.right: return [str(root.val)]
        else: return [str(root.val) + '->' + _ for child in (root.left, root.right) for _ in self.binaryTreePaths(child)]
