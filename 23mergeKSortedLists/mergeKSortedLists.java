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
        final var result = new ListNode(0);
        var current = result;
        for (final var $: (Iterable<ListNode>)Stream.of(lists).flatMap(list -> Stream.iterate(list, Objects::nonNull, $ -> $.next)).sorted(Comparator.comparingInt($ -> $.val))::iterator)
        {
            current.next = $;
            current = current.next;
        }
        return result.next;
    }
}
