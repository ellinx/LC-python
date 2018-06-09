"""
 Design and implement a data structure for Least Recently Used (LRU) cache.
 It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

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
class DataNode:
    def __init__(self, key, val):
        self.data = [key,val]
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = DataNode(0,0)
        self.tail = DataNode(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.keyToNode = dict()

    # remove data node from list
    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    # append data node at end of the list
    def appendNode(self, node):
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyToNode:
            return -1
        self.removeNode(self.keyToNode[key])
        self.appendNode(self.keyToNode[key])
        return self.keyToNode[key].data[1]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.keyToNode:
            if len(self.keyToNode)==self.capacity:
                if self.head.next!=self.tail:
                    self.keyToNode.pop(self.head.next.data[0])
                    self.removeNode(self.head.next)
                else:
                    return
            self.keyToNode[key] = DataNode(key,value)
            self.appendNode(self.keyToNode[key])
        else:
            self.keyToNode[key].data[1] = value
            self.removeNode(self.keyToNode[key])
            self.appendNode(self.keyToNode[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
