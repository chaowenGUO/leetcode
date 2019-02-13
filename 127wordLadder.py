import typing
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: typing.List[str]) -> int:
        import collections
        wordList = {*wordList}
        charSet = {char for word in wordList for char in word}
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord: return length
            else:
                for _ in range(len(word)):
                    for char in charSet:
                        nextWord = ''.join((word[:_], char, word[_ + 1:]))
                        if nextWord in wordList:
                            wordList.remove(nextWord)
                            queue += [nextWord, length + 1],
        return 0
