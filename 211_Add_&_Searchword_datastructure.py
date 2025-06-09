class WordDictionary(object):

    def __init__(self):
        self.g = {}


    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        if word[0] not in self.g:
            self.g[word[0]] = []

        for i in range(1, len(word)):
            if word[i] not in self.g:
                self.g[word[i]] = []
            self.g[word[i-1]].append(word[i])


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word)
        def dfs(v, i):
            if i == n:
                return True
            for u in self.g[v]:
                if u == word[i] or word[i] == ".":
                    dfs(u, i+1)
            return False
        if word[0] not in self.g:
            return False
        else:
            return dfs(word[0], 1)