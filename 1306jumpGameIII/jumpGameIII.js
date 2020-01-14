/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 */
var canReach = function(arr, start) {
    let queue = [start]
    let seen = new Set(queue)
    while (queue.length)
    {
        index = queue.shift()
        if (!arr[index]) return true
        else
        {
            const child = new Set([index + arr[index], index - arr[index]].filter(_ => 0 <= _ && _ < arr.length))
            seen.forEach(_ => child.delete(_))
            queue.push(...child)
            child.forEach(_ => seen.add(_))
        }
    }
    return false
};
