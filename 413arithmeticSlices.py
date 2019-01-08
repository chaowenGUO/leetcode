class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import functools
        if len(A) < 3: return 0
        else: return sum(functools.reduce(lambda result, _: [sum(result), [0, result[1] + 1][A[_] - A[_ - 1] == A[_ - 1] - A[_ - 2]]], range(2, len(A)), [0] * 2))
