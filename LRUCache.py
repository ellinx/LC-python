"""
 Design and implement a data structure for Least Recently Used (LRU) cache.
 It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
            otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
                    When the cache reached its capacity, it should invalidate the least recently used item
                    before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""
class DLNode:
    def __init__(self):
        self.data = None
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.head = DLNode()
        self.tail = DLNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0
        self.capacity = capacity

    def deleteNode(self, node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    def appendNode(self, node):
        pre = self.tail.prev
        pre.next, node.prev = node, pre
        node.next, self.tail.prev = self.tail, node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        ret = node.data[1]
        self.deleteNode(node)
        self.appendNode(node)
        return ret

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.data[1] = value
            self.deleteNode(node)
            self.appendNode(node)
            return
        node = DLNode()
        node.data = [key,value]
        self.map[key] = node
        self.appendNode(node)
        self.size += 1
        if self.size>self.capacity:
            node = self.head.next
            self.deleteNode(node)
            self.map.pop(node.data[0])
            self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
