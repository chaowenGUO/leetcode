/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

const lodash = require('lodash')

var isAnagram = function(s, t) {
    return lodash.isEqual(...[s, t].map(_ => lodash.countBy([..._])))
};
