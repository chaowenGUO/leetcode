class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = collections.defaultdict(list)
        for _ in strs: dictionary[frozenset(collections.Counter(_).items())] += _,
        return [*dictionary.values()]
