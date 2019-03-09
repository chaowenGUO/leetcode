class Solution:
    def longestWord(self, words: List[str]) -> str:
        return min(({*itertools.accumulate(word)} - {*words}, -len(word),  word) for word in words)[2]
