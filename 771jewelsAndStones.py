class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(item in J for item in S)
