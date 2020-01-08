/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function(s) {
    return Array.from(s.matchAll(/\d{2}#|\d/g), group => String.fromCodePoint(Number(group[0].replace('#', '')) +  'a'.codePointAt(0) - 1)).join('')
};
