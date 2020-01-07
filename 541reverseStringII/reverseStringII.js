/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var reverseStr = function(s, k) {
    s = [...s]
    for (let _ = 0; _ < s.length; _ += 2 * k) s.splice(_, 0, ...s.splice(_, k).reverse())
    return s.join('')
};
