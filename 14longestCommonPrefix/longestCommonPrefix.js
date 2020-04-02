/**
 * @param {string[]} strs
 * @return {string}
 */

const lodash = require('lodash')

var longestCommonPrefix = function(strs) {
    const result = lodash.zip(...lodash.takeWhile(lodash.zip(...strs.map(_ => [..._])), _ => Object.is(new Set(_).size, 1))).values().next()
    return result.done ? '' : result.value.join('')
};
