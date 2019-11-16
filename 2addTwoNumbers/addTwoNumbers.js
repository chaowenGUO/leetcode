/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    const result = new ListNode(null)
    let current = result
    let carry = 0
    while (l1 || l2 || carry)
    {
        if (l1)
        {
            carry += l1.val
            l1 = l1.next
        }
        if (l2)
        {
            carry += l2.val
            l2 = l2.next
        }
        current.next = new ListNode(carry % 10)
        carry = Math.trunc(carry / 10)
        current = current.next
    }
    return result.next
}
