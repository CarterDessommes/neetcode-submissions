class Node:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self):
        self.items = [Node(-1, -1) for i in range(10000)]
        

    def put(self, key: int, value: int) -> None:
        cur = self.items[key % len(self.items)]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = Node(key, value)
          

    def get(self, key: int) -> int:
        cur = self.items[key % len(self.items)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1
        
        

    def remove(self, key: int) -> None:
        cur = self.items[key % len(self.items)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
    
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)