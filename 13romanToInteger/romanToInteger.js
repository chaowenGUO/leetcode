/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const roman = Object.freeze({M:1000, D:500, C:100, L:50, X:10, V:5, I:1})
    return [...s].reverse().reduce((result, _) => [[_, result[1]].map(_ => roman[_]).reduce((a,b) => a - b) < 0 ? result[0] - roman[_] : result[0] + roman[_], _], [0, 'I'])[0]
};
