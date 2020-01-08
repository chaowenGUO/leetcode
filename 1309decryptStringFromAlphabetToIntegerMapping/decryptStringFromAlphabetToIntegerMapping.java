class Solution {
    public String freqAlphabets(String s) {
        final java.util.regex.Matcher matcher = java.util.regex.Pattern.compile("\\d{2}#|\\d").matcher(s);
        final StringBuilder result = new StringBuilder();
        while (matcher.find()) result.append(String.format("%c", Integer.parseInt(matcher.group().replace("#", "")) + 'a' - 1));
        return result.toString();
    }
}
