class Solution {
    public void rotate(int[][] matrix) {
        IntStream.range(0, matrix.length / 2).forEach($ -> {
            int[] tmp = matrix[$];
            matrix[$] = matrix[matrix.length - 1 - $];
            matrix[matrix.length - 1 - $] = tmp;});
        IntStream.range(0, matrix.length).forEach(row -> IntStream.range(row + 1, matrix.length).forEach(column -> {
            matrix[row][column] ^= matrix[column][row];
            matrix[column][row] ^= matrix[row][column];
            matrix[row][column] ^= matrix[column][row];}));
    }
}
