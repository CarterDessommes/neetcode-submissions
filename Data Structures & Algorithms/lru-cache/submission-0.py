class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.key_map = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.cap = capacity

        self.right.prev = self.left
        self.left.next = self.right
        
    def put(self, key: int, value: int) -> None:
        if key not in self.key_map:
            n = Node(key, value)
            self.key_map[key] = n
            self.add(n)
            if len(self.key_map) > self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.key_map[lru.key]
        else:
            n = self.key_map[key]
            n.val = value

            self.remove(n)
            self.add(n)
        


    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        self.remove(self.key_map[key])
        self.add(self.key_map[key])
        return self.key_map[key].val

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node

        
