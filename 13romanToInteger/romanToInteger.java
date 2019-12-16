enum Roman
{
    M(1000), D(500), C(100), L(50), X(10), V(5), I(1);
    private final int roman;
    private Roman(final int roman)
    {
        this.roman = roman;
    }
    public int get()
    {
        return this.roman;
    }
}

class Solution {
    public int romanToInt(String s) {
        return new StringBuilder(s).reverse().toString().codePoints().mapToObj($ -> String.format("%c", $)).reduce(new java.util.AbstractMap.SimpleEntry<>(0, "I"), (result, $) -> new java.util.AbstractMap.SimpleEntry<>(Stream.of($, result.getValue()).mapToInt($$ -> Roman.valueOf($$).get()).reduce((a,b) -> a - b).orElse(0) < 0 ? result.getKey() - Roman.valueOf($).get() : result.getKey() + Roman.valueOf($).get(), $), (x,y) -> x).getKey();
    }
}
