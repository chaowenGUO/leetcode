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
        final PriorityQueue<Integer> queue = new PriorityQueue();
        for(ListNode node: lists)
            while (node != null)
            {
                queue.offer(node.val);
                node = node.next;
            }
        final ListNode result = new ListNode(0);
        ListNode current = result;
        while (!queue.isEmpty())
        {
            current.next = new ListNode(queue.poll());
            current = current.next;
        }
        return result.next;
    }
}
