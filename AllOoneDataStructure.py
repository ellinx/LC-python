"""

Implement a data structure supporting the following operations:

1. Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
2. Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
3. GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
4. GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".

Challenge: Perform all these in O(1) time complexity.
"""
class DLNode:
    def __init__(self):
        self.data = [0, set()]
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        self.head = DLNode()
        self.tail = DLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.map:
            cur = self.map[key]
            cur.data[1].remove(key)
            val = cur.data[0]+1
            r = cur.next
            if len(cur.data[1])==0:
                #delete this node
                r.prev = cur.prev
                cur.prev.next = r
                cur = r.prev
        else:
            cur = self.head
            val = 1
        r = cur.next
        if r==self.tail or r.data[0]>val:
            self.map[key] = DLNode()
            self.map[key].data = [val, set()]
            self.map[key].data[1].add(key)
            # insert new node
            cur.next = self.map[key]
            self.map[key].prev = cur
            self.map[key].next = r
            r.prev = self.map[key]
        else:
            self.map[key] = r
            r.data[1].add(key)


    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.map:
            return
        cur = self.map[key]
        cur.data[1].remove(key)
        val = cur.data[0]-1
        l = cur.prev
        if len(cur.data[1])==0:
            #delete this node
            l.next = cur.next
            cur.next.prev = l
        if val==0:
            self.map.pop(key)
            return
        if l==self.head or l.data[0]<val:
            self.map[key] = DLNode()
            self.map[key].data = [val, set()]
            self.map[key].data[1].add(key)
            # insert new node
            cur = l.next
            l.next = self.map[key]
            self.map[key].prev = l
            self.map[key].next = cur
            cur.prev = self.map[key]
        else:
            self.map[key] = l
            l.data[1].add(key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        valSet = self.tail.prev.data[1]
        if len(valSet)==0:
            return ""
        for ret in valSet:
            return ret

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        valSet = self.head.next.data[1]
        if len(valSet)==0:
            return ""
        for ret in valSet:
            return ret


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
