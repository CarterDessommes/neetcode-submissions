class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        # same as usual trie
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
        cur.end = True

    def search(self, word: str) -> bool:
        
        # use dfs to handle the . case
        def dfs(j, root):
            cur = root

            # loop over word 
            for i in range(j, len(word)):
                char = word[i]
                # if its a .
                if char == ".":
                    # for each possible value
                    for child in cur.children.values():
                        # recurse to check it
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # if its a normal char just
                    # search like normal
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
        
            return cur.end
        
        return dfs(0, self.root)


        





       
        
