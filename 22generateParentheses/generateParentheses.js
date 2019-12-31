/**
 * @param {number} n
 * @return {string[]}
 */

const lodash = require('lodash')

var generateParenthesis = function(n) {
    const dp = Object.freeze([[''], ...Array.from({length:n}, () => [])])
    for (const i of Array(n + 1).keys())
        for (const j of Array(i).keys()) dp[i].push(...lodash.flatMap(dp[j], x => dp[i - j - 1].map(y => `(${x})${y}`)))
    return dp[dp.length - 1]
};
