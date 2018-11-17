# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = None
        while head:
            current = head
            head = head.next
            current.next = result
            result = current
        return result
 
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        else:
            result = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return result
