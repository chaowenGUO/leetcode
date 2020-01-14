class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = collections.deque([start])
        seen = {start}
        while queue:
            index = queue.popleft()
            if not arr[index]: return True
            else:
                child = {_ for _ in (index + arr[index], index - arr[index]) if 0 <= _ < len(arr)}
                queue += child - seen
                seen |= child
        return False
