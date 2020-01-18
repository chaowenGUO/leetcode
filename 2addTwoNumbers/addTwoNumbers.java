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
        final LinkedList<Integer> list = new LinkedList<>();
        int carry = 0;
        while (Objects.nonNull(l1) || Objects.nonNull(l2) || carry != 0)
        {
            if (Objects.nonNull(l1))
            {
                carry += l1.val;
                l1 = l1.next;
            }
            if (Objects.nonNull(l2))
            {
                carry += l2.val;
                l2 = l2.next;
            }
            list.offer(carry % 10);
            carry /= 10;
        }
        final ListNode result = new ListNode(0);
        ListNode current = result;
        for (final int $: list)
        {
            current.next = new ListNode($);
            current = current.next;
        }
        return result.next;
    }
}
