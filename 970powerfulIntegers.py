class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        return [*{x**i + y**j for i in range(18) for j in range(18) if x**i + y**j <= bound}]
