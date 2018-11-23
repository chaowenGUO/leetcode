# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        else:
            a, b = headA, headB
            while a and b and a !=b:
                a = a.next
                b = b.next
                if a == b: return b
                elif not a: a = headB
                elif not b: b = headA
            return a
