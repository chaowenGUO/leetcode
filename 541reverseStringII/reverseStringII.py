class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        *s, = s
        for _ in range(0, len(s), 2 * k): s[_:_ + k] = reversed(s[_:_ + k])
        return ''.join(s)
