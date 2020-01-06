/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    const result = new ListNode(null)
    let current = result
    current.next = head
    let a = null
    while ((a = current.next) && current.next.next)
    {
        current.next = curren.next.next
        a.next = a.next.next
        current.next.next = a
        current = a
    }
    return result.next
};
