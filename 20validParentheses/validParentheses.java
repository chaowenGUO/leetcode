class Solution {
    public boolean isValid(String s) {
        final HashMap<String, String> parentheses = new HashMap<>();
        parentheses.putIfAbsent("(",")");
        parentheses.putIfAbsent("[","]");
        parentheses.putIfAbsent("{","}");
        final LinkedList<String> stack = new LinkedList<>();
        for (final String $: java.util.stream.Stream.of(s.split("")).filter($ -> !$.isEmpty()).collect(java.util.stream.Collectors.toList()))
            if (parentheses.containsKey($)) stack.push(parentheses.get($));
            else
                if (stack.isEmpty() || !stack.pop().equals($)) return false;
        return stack.isEmpty();
    }
}
