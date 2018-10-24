"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        import itertools
        return max(itertools.chain(map(self.maxDepth, root.children), [0])) + 1 if root else 0
