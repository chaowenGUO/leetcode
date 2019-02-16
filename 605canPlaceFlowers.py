import typing
class Solution:
    def canPlaceFlowers(self, flowerbed: typing.List[int], n: int) -> bool:
        flowerbed = [0, *flowerbed, 0]
        count = 0
        for _ in range(1, len(flowerbed) - 1):
            if flowerbed[_ - 1] == flowerbed[_] == flowerbed[_ + 1] == 0:
                flowerbed[_] = 1
                count += 1
        return count >= n
