class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[_ ^ 1 for _ in reversed(row)] for row in A]
