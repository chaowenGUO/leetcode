class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        import collections
        dictionary = collections.defaultdict(list)
        for string in strs: dictionary[frozenset(collections.Counter(string).items())] += string,
        return [*dictionary.values()]
