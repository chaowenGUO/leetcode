enum Roman
{
    M(1000), CM(900), D(500), CD(400), C(100), XC(90), L(50), XL(40), X(10), IX(9), V(5), IV(4), I(1);
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
    public String intToRoman(int num) {
        StringBuilder result = new StringBuilder();
        for (final Roman roman: Roman.values())
        {
            result.append(java.util.stream.IntStream.range(0, num / roman.get()).mapToObj($ -> roman.name()).collect(java.util.stream.Collectors.joining()));
            num %= roman.get();
        }
        return result.toString();
    }
}
