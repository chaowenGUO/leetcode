class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr = *itertools.accumulate(arr, operator.xor),
        return [arr[j] ^ arr[i - 1] if i else arr[j] for i, j in queries]
