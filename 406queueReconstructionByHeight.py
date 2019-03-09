class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        for person in sorted(people, key = lambda _: (-_[0], _[1])): queue.insert(person[1], person)
        return queue
