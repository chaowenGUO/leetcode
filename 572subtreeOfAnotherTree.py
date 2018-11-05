class Solution:
    def isSame(self, p, q):
        if p and q: return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        else: return p == q
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s: return False
        elif self.isSame(s, t): return True
        else: return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
