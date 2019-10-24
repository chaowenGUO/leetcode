# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def generator(self):
    while self:
        yield self.val
        self = self.next
        
ListNode.__iter__ = generator

class Solution:            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1, l2 = map(list, (l1, l2))
        result = None
        carry = 0
        while l1 or l2 or carry:
            if l1: carry += l1.pop()
            if l2: carry += l2.pop()
            current = result
            result = ListNode(carry % 10)
            carry //= 10
            result.next = current
        return result
