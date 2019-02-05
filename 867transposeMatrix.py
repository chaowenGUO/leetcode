import typing
class Solution:
    def transpose(self, A: typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
        return [*map(list, zip(*A))]
