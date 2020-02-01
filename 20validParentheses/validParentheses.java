class Solution {
    public boolean isValid(String s) {
        final var parentheses = Map.ofEntries(Map.entry("{", "}"), Map.entry("[", "]"), Map.entry("(", ")"));
        final var stack = new LinkedList<String>();
        for (final var $: s.codePoints().mapToObj($ -> String.format("%c", $)).collect(Collectors.toList()))
        {
            if (parentheses.containsKey($)) stack.push(parentheses.get($));
            else if (stack.isEmpty() || !stack.pop().equals($)) return false;
        }
        return stack.isEmpty();
    }
}
