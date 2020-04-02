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
        final var list = new LinkedList<Integer>();
        var carry = 0;
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
        final var result = new ListNode(0);
        var current = result;
        for (final var $: list)
        {
            current.next = new ListNode($);
            current = current.next;
        }
        return result.next;
    }
}
