class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = {*wordList}
        result = []
        layer = {}
        layer[beginWord] = [[beginWord]]
        charSet = {char for word in wordList for char in word}
        while layer:
            newlayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord: result += layer[word]
                else:
                    for _ in range(len(word)):
                        for char in charSet:
                            nextWord = word[:_] + char + word[_ + 1:]
                            if nextWord in wordList: newlayer[nextWord] += [_ + [nextWord] for _ in layer[word]]
            wordList -= {*newlayer.keys()}
            layer = newlayer
        return result
