/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function(n, k) {
    let factorial = 1
    for (let _ = 2; !Object.is(_, n + 1); ++_) factorial *= _
    const result = []
    --k
    let elements = [...Array(n + 1).keys()].slice(1)
    while (elements.length)
    {
        factorial /= elements.length;
        [_, k] = [Math.trunc(k / factorial), k % factorial]
        result.push(elements.splice(_, 1))
    }
    return result.join('')
};
