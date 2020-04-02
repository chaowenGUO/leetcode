class Solution {
    public String longestPalindrome(String s) {
        final var replace = "$#" + java.util.regex.Pattern.compile("\\w").matcher(s).replaceAll(group -> group.group() + "#");
        var center = 0;
        var right = 0;
        final var radius = new int[replace.codePointCount(0, replace.length())];
        for (final var $: (Iterable<Integer>)IntStream.range(1, radius.length)::iterator)
        {
            radius[$] = right > $ ? Math.min(radius[2 * center - $], right - $) : 1;
            while ($ + radius[$] < radius.length && replace.codePointAt($ + radius[$]) == replace.codePointAt($ - radius[$])) ++radius[$];
            if ($ + radius[$] > right)
            {
                center = $;
                right = $ + radius[$];
            }
        }
        center = Arrays.stream(radius).boxed().collect(Collectors.toList()).indexOf(Arrays.stream(radius).max().orElse(0));
        return s.substring((center - radius[center]) / 2, (center + radius[center]) / 2 - 1);
    }
}
