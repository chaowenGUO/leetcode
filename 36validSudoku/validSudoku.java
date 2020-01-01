class Solution {
    public boolean isValidSudoku(char[][] board) {
        final List<String> seen = IntStream.range(0, board.length).boxed().flatMap(row -> IntStream.range(0, board[row].length).boxed().flatMap(column -> Stream.of(board[row][column] + ")" + column, row + "(" + board[row][column], row / 3 + "(" + board[row][column] + ")" + column / 3).filter($ -> !$.contains(".")))).collect(Collectors.toList());
        return seen.size() == seen.stream().collect(Collectors.toSet()).size();
    }
}
