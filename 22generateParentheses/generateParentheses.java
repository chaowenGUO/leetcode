class Solution {
    public List<String> generateParenthesis(int n) {
        final List<ArrayList<String>> dp = java.util.stream.IntStream.range(0, n + 1).mapToObj($ -> new ArrayList<String>()).collect(java.util.stream.Collectors.toList());
        dp.get(0).add("");
        java.util.stream.IntStream.range(0, n + 1).forEach(i -> java.util.stream.IntStream.range(0, i).forEach(j -> dp.get(i).addAll(dp.get(j).stream().flatMap(x -> dp.get(i - 1 - j).stream().map(y -> "(" + x + ")" + y)).collect(java.util.stream.Collectors.toList()))));
        return dp.get(dp.size() - 1);
    }
}
