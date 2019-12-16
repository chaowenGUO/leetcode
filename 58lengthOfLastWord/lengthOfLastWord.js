/**
 * @param {string} s
 * @return {number}
 */

const lodash = require('lodash')

var lengthOfLastWord = function(s) {
    return lodash.takeRightWhile(s.trim(), _ => !Object.is(_, ' ')).length
};
