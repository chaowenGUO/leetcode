class Solution:
    def constructRectangle(self, area: 'int') -> 'List[int]':
        import math
        W = int(math.sqrt(area))
        while area % W: W -= 1
        return area // W, W
