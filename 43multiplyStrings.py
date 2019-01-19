class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        import operator
        result = [0] * sum(map(len, (num1, num2)))
        for index1, value1 in enumerate(reversed(num1)):
            for index2, value2 in enumerate(reversed(num2)):
                result[index1 + index2] += operator.mul(*map(int, (value1, value2)))
                result[index1 + index2 + 1] += result[index1 + index2] // 10
                result[index1 + index2] %= 10
                
        while result and result[-1] == 0: result.pop()
        return ''.join(map(str, reversed(result))) if result else '0'
