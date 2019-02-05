import typing
class Solution:
    def flipAndInvertImage(self, A: typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
        return [[_ ^ 1 for _ in reversed(row)] for row in A]
