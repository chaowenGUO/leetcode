class Solution {
    public int myAtoi(String str) {
        final var matcher = java.util.regex.Pattern.compile("^[+-]?\\d+").matcher(str.strip());
        final java.math.BigInteger result = matcher.find() ? new java.math.BigInteger(matcher.group()) : java.math.BigInteger.ZERO;
        return Stream.of(java.math.BigInteger.valueOf(Integer.MIN_VALUE), java.math.BigInteger.valueOf(Integer.MAX_VALUE), result).sorted().skip(1).findFirst().orElse(java.math.BigInteger.ZERO).intValueExact();
    }
}
