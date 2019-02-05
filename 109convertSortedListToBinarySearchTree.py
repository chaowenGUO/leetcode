# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        elif not head.next: return TreeNode(head.val)
        else:
            fast, slow = head.next.next, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            fast = slow.next
            slow.next = None
            root = TreeNode(fast.val)
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(fast.next)
            return root
