/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    matrix.reverse()
    for (let row = 0; !Object.is(row, matrix.length); ++row)
        for (let column = row; !Object.is(column, matrix.length); ++column) [matrix[row][column], matrix[column][row]] = [matrix[column][row], matrix[row][column]]
};
