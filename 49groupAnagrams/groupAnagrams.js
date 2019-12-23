/**
 * @param {string[]} strs
 * @return {string[][]}
 */

const lodash = require('lodash')

var groupAnagrams = function(strs) {
    return Object.values(lodash.groupBy(strs, _ => [..._].sort().join('')))
};
