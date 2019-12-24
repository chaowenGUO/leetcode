class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('\W', '', s).lower()
        return s == s[::-1]
