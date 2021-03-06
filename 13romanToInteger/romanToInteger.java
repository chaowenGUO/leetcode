class Solution {
    public int romanToInt(String s) {
        final var roman = Collections.unmodifiableMap(Map.ofEntries(Map.entry("M", 1000), Map.entry("D", 500), Map.entry("C", 100), Map.entry("L", 50), Map.entry("X", 10), Map.entry("V", 5), Map.entry("I", 1)));
        return new StringBuilder(s).reverse().toString().codePoints().mapToObj($ -> String.format("%c", $)).reduce(Map.entry(0, "I"), (result, $) -> Map.entry(roman.get($) < roman.get(result.getValue()) ? result.getKey() - roman.get($) : result.getKey() + roman.get($) ,$), (x, y) -> x).getKey();
    }
}
