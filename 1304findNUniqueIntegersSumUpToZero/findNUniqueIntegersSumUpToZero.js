/**
 * @param {number} n
 * @return {number[]}
 */

const lodash = require('lodash')

var sumZero = function(n) {
    return lodash.range(1 - n, n, 2)
};
