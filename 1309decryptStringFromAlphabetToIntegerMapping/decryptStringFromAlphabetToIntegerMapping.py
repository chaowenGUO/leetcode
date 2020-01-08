class Solution:
    def freqAlphabets(self, s: str) -> str:
        return ''.join(chr(int(group[0].replace('#','')) + ord('a') - 1) for group in re.finditer('\d{2}#|\d', s))
