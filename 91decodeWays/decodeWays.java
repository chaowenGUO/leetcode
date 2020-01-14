class Solution {
    public int numDecodings(String s) {
        List<String> ss = s.codePoints().mapToObj($ -> String.format("%c", $)).collect(Collectors.toList());
        if (ss.get(0).equals("0")) return 0;
        else
        {
            int a = 1, b = 1, c = 0;
            for (int $ = 1; $ != ss.size(); ++$)
            {
                if (!ss.get($).equals("0")) c = b;
                final String subList = ss.subList($ - 1, $  + 1).stream().collect(Collectors.joining());
                if (0 <= subList.compareTo("10") && subList.compareTo("26") <= 0) c += a;
                a = b;
                b = c;
                c = 0;
            }
            return b;
        }
    }
}
