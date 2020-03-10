class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        return [''.join(_) for _ in itertools.product(*(phone.get(int(_)) for _ in digits))] if digits else []
