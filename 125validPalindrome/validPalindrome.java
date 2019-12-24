class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("\\W", "").toLowerCase();
        return s.equals(new StringBuilder(s).reverse().toString());
    }
}
