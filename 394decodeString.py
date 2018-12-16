class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        while '[' in s: s = re.sub('(\d+)\[([^\[\]]*)\]', lambda _: int(_.group(1)) * _.group(2), s)
        return s
