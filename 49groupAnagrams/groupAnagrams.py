class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort(key = lambda _:sorted(_))
        return [[*group] for _, group in itertools.groupby(strs, lambda _:sorted(_))]
