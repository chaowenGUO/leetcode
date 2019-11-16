class Solution {
    public int myAtoi(String str) {
        final java.util.regex.Matcher matcher = java.util.regex.Pattern.compile("^[+-]?\\d+").matcher(str.trim());
        final java.math.BigInteger result = new java.math.BigInteger(matcher.find() ? matcher.group() : "0");
        return java.util.stream.Stream.of(result, java.math.BigInteger.valueOf(Integer.MAX_VALUE), java.math.BigInteger.valueOf(Integer.MIN_VALUE)).sorted().skip(1).findFirst().orElse(java.math.BigInteger.ZERO).intValue();
    }
}
