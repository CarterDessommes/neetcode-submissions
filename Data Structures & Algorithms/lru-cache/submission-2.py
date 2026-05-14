class Node:
    def __init__(self, nxt, prev, val, key):
        self.nxt = nxt
        self.key = key
        self.prev = prev
        self.val = val


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(None, None, 0, 0)
        self.right = Node(None, self.left, 0, 0)
        self.left.nxt = self.right
    
    def remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
    
    def add(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.nxt = node
        nxt.prev = node
        node.nxt = nxt
        node.prev = prev

        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            node = Node(None, None, value, key)
            self.add(node)
            self.cache[key] = node
            if len(self.cache) > self.cap:
                to_remove = self.left.nxt
                key = self.left.nxt.key
                del self.cache[key]
                self.remove(to_remove)

        
