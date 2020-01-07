class Solution {
    public String reverseStr(String s, int k) {
        final List<String> result = s.codePoints().mapToObj($ -> String.format("%c", $)).collect(Collectors.toList());
        for (int $ = 0; $ < result.size(); $ += 2 * k) Collections.reverse(result.subList($, Math.min($ + k, result.size())));
        return result.stream().collect(Collectors.joining());
    }
}
