# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def generator(self):
    while self:
        yield self
        self = self.next

ListNode.__iter__ = generator
            
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = current = ListNode(None)
        for current.next in heapq.merge(*(_ for _ in lists if _ is not None), key = lambda _:_.val): current = current.next
        return result.next
