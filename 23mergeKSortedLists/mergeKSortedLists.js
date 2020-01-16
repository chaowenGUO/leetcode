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
        yield node
        node = node.next
    }
}

var mergeKLists = function(lists) {
    const queue = []
    for (const _ of lists.filter(_ => !Object.is(_, null))) queue.push(..._)
    queue.sort((a,b) => a.val - b.val)
    const result = new ListNode(null)
    let current = result
    while (queue.length)
    {
        current.next = queue.shift()
        current = current.next
    }
    current.next = null
    return result.next
};
