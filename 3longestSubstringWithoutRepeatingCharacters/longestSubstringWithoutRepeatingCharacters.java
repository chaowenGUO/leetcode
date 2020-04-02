class Solution {
    public int lengthOfLongestSubstring(String s) {
        var result = 0;
        var left = 0;
        var right = 0;
        final var characters = new HashSet<Integer>();
        while (right < s.codePointCount(0, s.length()))
            if (!characters.contains(s.codePointAt(right)))
            {
                characters.add(s.codePointAt(right++));
                result = Math.max(result, characters.size());
            }
            else characters.remove(s.codePointAt(left++));
        return result;
    }
}
