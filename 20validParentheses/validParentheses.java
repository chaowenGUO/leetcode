class Solution {
    public boolean isValid(String s) {
        final HashMap<String, String> parentheses = new HashMap<>();
        parentheses.putIfAbsent("(", ")");
        parentheses.putIfAbsent("[", "]");
        parentheses.putIfAbsent("{", "}");
        final LinkedList<String> stack = new LinkedList<>();
        for (final String $: s.codePoints().mapToObj($ -> String.format("%c", $)).collect(Collectors.toList()))
        {
            if (parentheses.containsKey($)) stack.push(parentheses.get($));
            else
                if (stack.isEmpty() || !stack.pop().equals($)) return false;
        }
        return stack.isEmpty();
    }
}
