class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        vowels = re.findall('[aeiouAEIOU]', s)
        return re.sub('[aeiouAEIOU]', lambda _: vowels.pop(), s)
