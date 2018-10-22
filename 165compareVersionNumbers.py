class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        import itertools
        version = (map(int, _.split('.')) for _ in (version1, version2))
        for _ in itertools.zip_longest(*version, fillvalue = 0):
            if _[0] > _[1]: return 1
            elif _[0] < _[1]: return -1
        return 0
