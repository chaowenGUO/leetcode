/**
 * @param {string[]} strs
 * @return {string}
 */

const lodash = require('lodash')

var longestCommonPrefix = function(strs) {
    try
    {
        return lodash.zip(...lodash.takeWhile(lodash.zip(...strs.map(_ => [..._])), _ => Object.is(new Set(_).size, 1)))[0].join('')
    }
    catch
    {
        return ''
    }
};
