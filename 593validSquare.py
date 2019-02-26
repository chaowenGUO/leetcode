class Solution:
    def distance(self, p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        data = {self.distance(p1, p2), self.distance(p1, p3), self.distance(p1, p4), self.distance(p2, p3), self.distance(p2, p4), self.distance(p3, p4)}
        return 0 not in data and len(data) == 2
