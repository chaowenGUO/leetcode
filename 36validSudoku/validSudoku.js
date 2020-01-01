/**
 * @param {character[][]} board
 * @return {boolean}
 */
const lodash = require('lodash')

var isValidSudoku = function(board) {
    const seen = lodash.flatMap(board, (row, i) => lodash.flatMap(row, (column, j) => [[column, j], [i, column], [Math.trunc(i / 3), Math.trunc(j / 3), column]].filter(_ => !_.includes('.'))))
    return Object.is(seen.length, lodash.uniqWith(seen, lodash.isEqual).length)
};
