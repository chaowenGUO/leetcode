class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) return s;
        else
        {
            final var result = IntStream.range(0, numRows).mapToObj($ -> "").toArray(String[]::new);
            var row = 0;
            var direction = 1;
            for (final var $: (Iterable<String>)s.codePoints().mapToObj($ -> String.format("%c", $))::iterator)
            {
                result[row] += $;
                if (row == 0) direction = 1;
                else if (row == numRows - 1) direction = -1;
                row += direction;
            }
            return Stream.of(result).collect(Collectors.joining());
        }
    }
}
