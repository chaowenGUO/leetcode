/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        final LinkedList<Integer> linkedList = new LinkedList<>();
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0)
        {
            if (l1 != null)
            {
                carry += l1.val;
                l1 = l1.next;
            }
            if (l2 != null)
            {
                carry += l2.val;
                l2 = l2.next;
            }
            linkedList.offer(carry % 10);
            carry /= 10;
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
