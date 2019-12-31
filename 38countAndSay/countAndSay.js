/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    let result = '1'
    for (const _ of Array(n - 1).keys()) result = result.replace(/(.)\1*/g, (group0, group1) => group0.length + group1)
    return result
};
