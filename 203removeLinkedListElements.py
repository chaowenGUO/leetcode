# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        result = current = ListNode(None)
        result.next = head
        while current.next:
            if current.next.val == val: current.next = current.next.next
            else: current = current.next
        return result.next
