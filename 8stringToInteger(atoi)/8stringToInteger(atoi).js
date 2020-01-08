/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    let result = str.trim().match(/^[+-]?\d+/)
    result = BigInt(result ? result[0] : 0)
    return [result, -1n << 31n, (1n << 31n) - 1n].sort((a,b) => a - b)[1]
};
