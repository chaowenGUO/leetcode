/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        final LinkedList<Integer> linkedList = new LinkedList<>();
        while (l1 != null && l2 != null)
        {
            if (l1.val < l2.val)
            {
                linkedList.offer(l1.val);
                l1 = l1.next;
            }
            else
            {
                linkedList.offer(l2.val);
                l2 = l2.next;
            }
        }
        ListNode l = l1 != null ? l1 : l2;
        while (l != null)
        {
            linkedList.offer(l.val);
            l = l.next;
        }
        final ListNode result = new ListNode(0);
        ListNode current = result;
        for (final int $: linkedList)
        {
            current.next = new ListNode($);
            current = current.next;
        }
        return result.next;
    }
}
