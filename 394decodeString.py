class Solution:
    def decodeString(self, s: str) -> str:
        while '[' in s: s = re.sub('(\d+)\[([^\[\]]*)\]', lambda _: int(_.group(1)) * _.group(2), s)
        return s
