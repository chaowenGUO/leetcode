class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        return [*{x**i + y**j for i in range(20) for j in range(20) if x**i + y**j <= bound}]
