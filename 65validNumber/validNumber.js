/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    return /^[+-]?(\.\d+|\d+\.?\d*)(e[+-]?\d+)?$/.test(s.trim())
};
