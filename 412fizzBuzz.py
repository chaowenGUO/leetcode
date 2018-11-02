class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['Fizz' * (not _ % 3) + 'Buzz' * (not _ % 5) or str(_) for _ in range(1, n + 1)]