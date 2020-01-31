import numpy

class Solution:
    def longestPalindrome(self, s: str) -> str:
        replace = '$#' + re.sub('\w', lambda group: group[0] + '#', s)
        center, right = 0, 0
        radius = [0] * len(replace)
        for _ in range(1, len(replace)):
            radius[_] = min(radius[2 * center - _], right - _) if right > _ else 1
            while _ + radius[_] < len(replace) and replace[_ + radius[_]] == replace[_ - radius[_]]: radius[_] += 1
            if _ + radius[_] > right:
                center = _
                right = _ + radius[_]
        center = numpy.argmax(radius)
        return s[(center - radius[center]) // 2: (center + radius[center]) // 2 - 1]
