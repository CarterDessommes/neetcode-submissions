class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in cur.children:
                cur.children[char] = TrieNode()
            if i == len(word) - 1:
                cur.children[char].end = True
            cur = cur.children[char]


    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in cur.children:
                return False
            if i == len(word) - 1:
                return cur.children[char].end
            
            cur = cur.children[char]

        return False



    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        
        return True
        