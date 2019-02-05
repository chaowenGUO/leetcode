import typing
class Solution:
    def largestNumber(self, nums: typing.List[int]) -> str:
        return str(int(''.join(sorted(map(str, nums), key = lambda _: _ * 9, reverse = True))))
