enum Roman
{
    M(1000), CM(900), D(500), CD(400), C(100), XC(90), L(50), XL(40), X(10), IX(9), V(5), IV(4), I(1);
    private final int roman;
    private Roman(final int roman)
    {
        this.roman = roman;
    }
    public int value()
    {
        return this.roman;
    }
}

class Solution {
    public String intToRoman(int num) {
        final var result = new StringBuilder();
        for (final var $: Roman.values())
        {
            result.append($.name().repeat(num / $.value()));
            num %= $.value();
        }
        return result.toString();
    }
}
