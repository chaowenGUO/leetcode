/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    return !s.trim().search(/^[+-]?(\.\d+|\d+\.?\d*)(e[+-]?\d+)?$/)
};
