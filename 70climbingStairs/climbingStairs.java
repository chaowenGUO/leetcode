class Solution {
    public int climbStairs(int n) {
        return java.util.stream.IntStream.range(0, n).boxed().reduce(Arrays.asList(1, 1), (acc, $) -> Arrays.asList(acc.get(1), acc.stream().mapToInt(Integer::valueOf).sum()), (x, y) -> x).get(0);
    }
}
