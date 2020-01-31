class Solution {
    public String countAndSay(int n) {
        var result = "1";
        for (var $ = 0; $ != n - 1; ++$) result = java.util.regex.Pattern.compile("(.)\\1*").matcher(result).replaceAll(group -> group.group().length() + group.group(1));
        return result;
    }
}
