class Solution {
    public int lengthOfLastWord(String s) {
        return Math.toIntExact(new StringBuilder(s.strip()).reverse().toString().codePoints().takeWhile($ -> $ != " ".codePointAt(0)).count());
    }
}
