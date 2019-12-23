class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        return Stream.of(strs).collect(Collectors.groupingBy($ -> $.codePoints().boxed().collect(Collectors.groupingBy(Function.identity(), Collectors.counting())))).values().stream().collect(Collectors.toList());
    }
}
