/**
 * @param {number} n
 * @return {string[]}
 */

const lodash = require('lodash')

var generateParenthesis = function(n) {
    const dp = Object.freeze([['']].concat(Array.from({length:n}, () => [])))
    for (let i = 0; !Object.is(i, n + 1); ++i)
        for (let j = 0; !Object.is(j, i); ++j) dp[i].push(...lodash.flatMap(dp[j], x => dp[i - j - 1].map(y => `(${x})${y}`)))
    return dp[dp.length - 1]
};
