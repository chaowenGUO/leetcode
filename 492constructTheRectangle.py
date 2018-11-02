class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        W = int(math.sqrt(area))
        while area % W: W -= 1
        return area // W, W
