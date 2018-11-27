class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for _ in range(1, len(flowerbed) - 1):
            if flowerbed[_ - 1] == flowerbed[_] == flowerbed[_ + 1] == 0:
                flowerbed[_] = 1
                count += 1
        return count >= n
