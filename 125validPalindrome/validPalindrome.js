/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.replace(/\W/g, '').toLowerCase()
    return Object.is(s, [...s].reverse().join(''))
};
