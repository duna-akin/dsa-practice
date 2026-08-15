class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict() # key to node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.tail.prev = self.head
        self.head.next = self.tail
    
    def remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def insert(self, node):
        p, n = self.tail.prev, self.tail
        p.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = p

    def get(self, key):
        if key not in self.cache:
            return -1
        mru = self.cache[key]
        self.remove(mru)
        self.insert(mru)
        return mru.val

    def put(self, key, val):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if self.capacity < len(self.cache):
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
