/**
 * @param {string[]} strs
 * @return {string}
 */

const lodash = require('lodash')

var longestCommonPrefix = function(strs) {
    const result = lodash.chain(strs.map(lodash.unary(Array.from))).unzip().takeWhile(_ => Object.is(new Set(_).size, 1)).unzip().next()
    return result.done ? '' : result.value.join('')
};
