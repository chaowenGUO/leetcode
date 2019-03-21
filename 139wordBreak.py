import functools

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return functools.reduce(lambda result, i: [*result, any(result[j] and s[j:i] in wordDict for j in range(i))], range(1, len(s) + 1), [True])[-1]
