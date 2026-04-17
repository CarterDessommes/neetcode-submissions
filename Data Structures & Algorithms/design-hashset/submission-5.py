class Node:
    def __init__(self, key):
        self.next = None
        self.key = key



class MyHashSet:

    def __init__(self):
        self.set = [Node(-1) for i in range(10000)]
        

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            cur = cur.next
            if cur.key == key:
                return  
        cur.next = Node(key)
        
        
    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = None
                return
            cur = cur.next
        
        

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            cur = cur.next
            if cur.key == key:
                return True
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)