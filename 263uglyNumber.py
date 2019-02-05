class Solution:
    def isUgly(self, num: int) -> bool:
        for _ in 2, 3, 5:
            while num % _ == 0 < num: num //= _
        return num == 1
