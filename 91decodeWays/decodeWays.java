class Solution {
    public int numDecodings(String s) {
        String[] ss = s.codePoints().mapToObj($ -> String.format("%c", $)).toArray(String[]::new);
        if (ss[0].equals("0")) return 0;
        else
        {
            LinkedList<Integer> result = IntStream.of(1, 1, 0).boxed().collect(Collectors.toCollection(LinkedList::new));
            for (int $ = 1; $ != ss.length; ++$)
            {
                if (!ss[$].equals("0")) result.set(result.size() - 1, result.get(1));
                final String subList = ss[$ - 1] + ss [$];
                if (0 <= subList.compareTo("10") && subList.compareTo("26") <= 0) result.set(result.size() - 1, result.get(2) + result.get(0));
                result.poll();
                result.offer(0);
            }
            return result.get(1);
        }
    }
}
