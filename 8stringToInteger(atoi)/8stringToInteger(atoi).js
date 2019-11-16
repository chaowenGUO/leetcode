/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    let result = /^[+-]?\d+/.exec(str.trim())
    result = BigInt(result ? result[0] : 0)
    return [result, -1n << 31n, (1n << 31n) - 1n].sort((a, b) => a - b)[1]
};
