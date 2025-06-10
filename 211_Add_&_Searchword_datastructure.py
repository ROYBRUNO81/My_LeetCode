class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.is_end = False

    def add_child(self, letter: str):
        if letter not in self.children:
            self.children[letter] = TrieNode(letter)
        return self.children[letter]

    def has_child(self, letter: str):
        return letter in self.children

    def get_child(self, letter: str):
        return self.children.get(letter)

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode("-")


    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """


        node = self.root
        n = len(word)
        for i in range(n):
            if node.has_child(word[i]):
                node = node.get_child(word[i])
            else:
                node = node.add_child(word[i])
                if i == n - 1:
                    node.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word)

        def dfs(node, i):
            if i == n:
                if node.is_end:
                    return True
                else:
                    return False

            for child in node.children:
                if word[i] == child or word[i] == ".":
                    if dfs(node.get_child(child), i+1):
                        return True
            return False

        if word[0] == ".":
            my_return = False
            for child in self.root.children:
                my_return = my_return or dfs(self.root.get_child(child), 1)
            return my_return
        else:
            return dfs(self.root, 0)

wd = WordDictionary()
wd.addWord("")
print(wd.search("."))