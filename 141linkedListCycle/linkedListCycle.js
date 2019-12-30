/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let [fast, slow] = Array(2).fill(head)
    while (fast && fast.next)
    {
        fast = fast.next.next
        slow = slow.next
        if (Object.is(fast, slow)) return true
    }
    return false
};
