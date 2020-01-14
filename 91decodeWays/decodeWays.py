class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        else:
            a, b, c = 1, 1, 0
            for _ in range(1, len(s)):
                if s[_] != '0': c = b	
                if '10' <= s[_ - 1:_ + 1] <= '26': c += a		
                a, b, c = b, c, 0 
            return b
