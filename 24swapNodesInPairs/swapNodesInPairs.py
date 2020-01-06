# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        result = current = ListNode(None)
        result.next = head
        while (a := current.next) and current.next.next:
            current.next = current.next.next
            a.next = a.next.next
            current.next.next = a
            current = a
        return result.next
            
