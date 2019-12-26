class Solution {
    private static Map<Integer, Long> groupBy(String s)
    {
        return s.codePoints().boxed().collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
    }
                                              
    public boolean isAnagram(String s, String t) {
        return this.groupBy(s).equals(this.groupBy(t));
    } 
}
