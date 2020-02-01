/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    const vowels = Array.from(s.matchAll(/[aeiou]/gi), group => group[0])
    return s.replace(/[aeiou]/gi, group => vowels.pop())
};
