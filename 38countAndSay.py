import functools

class Solution:
    def countAndSay(self, n: int) -> str:
        return functools.reduce(lambda result, _: ''.join(str(sum(1 for _ in group)) + key for key, group in itertools.groupby(result)), range(n - 1), '1')
