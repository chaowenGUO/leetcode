/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    return Array.from({length: 1 << n}, ($, _) => _ >> 1 ^_)
};
