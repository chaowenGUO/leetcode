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

const lodash = require('lodash')

ListNode.prototype[Symbol.iterator] = function*()
{
    let _ = this
    while (_)
    {
        yield _
        _ = _.next
    }
}

var mergeKLists = function(lists) {
    const result = new ListNode(null)
    let current = result
    for (const _ of lodash.chain(lists).filter(_ => !Object.is(_, null)).flatMap(lodash.unary(Array.from)).sortBy([_ => _.val]))
    {
        current.next = _
        current = current.next
    }
    return result.next
};
