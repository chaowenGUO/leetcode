/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */

ListNode.prototype[Symbol.iterator] = function* ()
{
    let node = this
    while (node)
    {
        yield node.val
        node = node.next
    }
}

var mergeKLists = function(lists) {
    const queue = []
    for (const _ of lists.filter(_ => !Object.is(_, null))) queue.push(..._)
    queue.sort((a,b) => a - b)
    const result = new ListNode(null)
    let current = result
    for (const _ of queue)
    {
        current.next = new ListNode(_)
        current = current.next
    }
    return result.next
};
