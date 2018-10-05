"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        result, level = [], [root]
        while root and level:
            result += [[node.val for node in level]]
            level = [child for node in level for child in node.children if child]
        return result
