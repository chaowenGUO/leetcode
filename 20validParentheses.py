class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {'{':'}', '[':']', '(':')'}
        stack = []
        for bracket in s:
            if bracket in dictionary: stack += dictionary.get(bracket),
            else:
                if not stack or stack.pop() != bracket: return False
        return not stack
