class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version = (map(int, _.split('.')) for _ in (version1, version2))
        for _ in itertools.zip_longest(*version, fillvalue = 0):
            if _[0] > _[1]: return 1
            elif _[0] < _[1]: return -1
        return 0
