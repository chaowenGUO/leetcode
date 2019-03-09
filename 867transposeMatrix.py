class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [*map(list, zip(*A))]
