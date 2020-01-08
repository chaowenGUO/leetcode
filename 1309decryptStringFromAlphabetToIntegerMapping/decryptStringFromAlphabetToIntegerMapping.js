/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function(s) {
    return Array.from(s.matchAll(/\d{2}#|\d/g), _ => String.fromCodePoint(Number(_[0].replace('#', '')) +  'a'.codePointAt(0) - 1)).join('')
};
