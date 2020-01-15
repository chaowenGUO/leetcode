class Solution {
    public List<String> generateParenthesis(int n) {
        final List<List<String>> dp = IntStream.range(0, n + 1).mapToObj($ -> Collections.<String>emptyList().stream().collect(Collectors.toList())).collect(Collectors.toList());
        dp.get(0).add("");
        IntStream.range(0, n + 1).forEach(i -> IntStream.range(0, i).forEach(j -> dp.get(i).addAll(dp.get(j).stream().flatMap(x -> dp.get(i - j - 1).stream().map(y -> "(" + x + ")" + y)).collect(Collectors.toList()))));
        return dp.get(dp.size() - 1);
    }
}
