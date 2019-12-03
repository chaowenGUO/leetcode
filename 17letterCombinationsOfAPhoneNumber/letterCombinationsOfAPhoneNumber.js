/**
 * @param {string} digits
 * @return {string[]}
 */
const lodash = require('lodash')

var letterCombinations = function(digits) {
    const phone = Object.freeze({2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'});
    return digits.length ? [...digits].reduce((result, digit) => lodash.flatMap(result, x => Array.from(phone[digit], y => x + y)), ['']) : []
};
