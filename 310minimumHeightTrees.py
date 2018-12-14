class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        else:
            adjacent = [set() for _ in range(n)]
            for _ in edges:
                adjacent[_[0]].add(_[1])
                adjacent[_[1]].add(_[0])
            leaves = [_ for _ in range(n) if len(adjacent[_]) == 1]
            while n > 2:
                n -= len(leaves)
                newLeaves = []
                for _ in leaves:
                    node = adjacent[_].pop()
                    adjacent[node].remove(_)
                    if len(adjacent[node]) == 1: newLeaves += node,
                leaves = newLeaves
            return leaves
