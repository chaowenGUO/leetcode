class Solution {
    public String reverseVowels(String s) {
        final var matcher = java.util.regex.Pattern.compile("[aeiou]", java.util.regex.Pattern.CASE_INSENSITIVE).matcher(s);
        final var vowels = matcher.results().map(group -> group.group()).collect(Collectors.toCollection(LinkedList::new));
        Collections.reverse(vowels);
        matcher.reset();
        return matcher.replaceAll(group -> vowels.pop());
    }
}
