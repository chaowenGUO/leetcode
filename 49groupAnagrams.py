class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = collections.defaultdict(list)
        for string in strs: dictionary[frozenset(collections.Counter(string).items())] += string,
        return [*dictionary.values()]
