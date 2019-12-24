class Solution {
    public int climbStairs(int n) {
        return Stream.iterate(Arrays.asList(1, 1), result -> Arrays.asList(result.get(1), result.stream().mapToInt(Integer::intValue).sum())).mapToInt($ -> $.get(1)).limit(n).reduce((a,b) -> b).orElse(0);
    }
}
