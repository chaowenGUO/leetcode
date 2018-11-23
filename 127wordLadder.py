class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        import collections
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        wordSet = {char for word in wordList for char in word}
        while queue:
            word, length = queue.popleft()
            if word == endWord: return length
            else:
                for _ in range(len(word)):
                    for char in wordSet:
                        nextWord = word[:_] + char + word[_ + 1:]
                        if nextWord in wordList:
                            wordList.remove(nextWord)
                            queue += [nextWord, length + 1],
        return 0
