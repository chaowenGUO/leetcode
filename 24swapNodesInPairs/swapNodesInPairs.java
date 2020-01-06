/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        final ListNode result = new ListNode(0);
        ListNode current = result;
        current.next = head;
        ListNode a;
        while ((a = current.next) != null && current.next.next != null)
        {
            current.next = current.next.next;
            a.next = a.next.next;
            current.next.next = a;
            current = a;
        }
    return result.next;
    }
}
