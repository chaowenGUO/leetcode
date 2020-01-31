class Solution {
    public String longestPalindrome(String s) {
        final String replace = "$#" + s.replaceAll("\\w", "$0#");
        int center = 0, right = 0;
        int[] radius = new int[replace.codePointCount(0, replace.length())];
        for (int $ = 1; $ != radius.length; ++$)
        {
            radius[$] = right > $ ? Math.min(radius[2 * center - $], right - $) : 1;
            while ($ + radius[$] < radius.length && replace.codePointAt($ + radius[$]) == replace.codePointAt($ - radius[$])) radius[$] += 1;
            if ($ + radius[$] > right)
            {
                center = $;
                right = $ + radius[$];
            }
        }
        center = IntStream.range(0, radius.length).filter($ -> radius[$] == Arrays.stream(radius).max().orElse(0)).findFirst().orElse(0);
        return s.substring((center - radius[center]) / 2, (center + radius[center]) / 2 - 1);
    }
}
