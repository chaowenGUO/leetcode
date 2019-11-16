class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'{':'}', '[':']', '(':')'}
        stack = []
        for _ in s:
            if _ in parentheses: stack += parentheses.get(_),
            else:
                if not stack or stack.pop() != _: return False
        return not stack
