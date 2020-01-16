/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        final PriorityQueue<ListNode> queue = new PriorityQueue<>(Comparator.comparing($ -> $.val));
        for (ListNode $: lists)
            while ($ != null)
            {
                queue.offer($);
                $ = $.next;
            }
        final ListNode result = new ListNode(0);
        ListNode current = result;
        while (!queue.isEmpty())
        {
            current.next = queue.poll();
            current = current.next;
        }
        current.next = null;
        return result.next;
    }
}
