import typing
class Solution:
    def letterCombinations(self, digits: str) -> typing.List[str]:
        import functools, itertools
        dictionary = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        return functools.reduce(lambda result, digit: [''.join(_) for _ in itertools.product(result, dictionary.get(digit))], digits, ['']) if digits else []
