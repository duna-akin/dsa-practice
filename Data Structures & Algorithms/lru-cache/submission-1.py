class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.head = Node()
        self.tail = Node()
        self.tail.prev = self.head
        self.head.next = self.tail

    def remove_node(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # inserts node right before tail dummy node
    def insert_node_end(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        node.next = nxt
        node.prev = prev
        nxt.prev = node
    
    def get(self, key):
        # move node to end and return (most recently used) if key exists
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node_end(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key, value):
        # remove if key already exists
        if key in self.cache:
            self.remove_node(self.cache[key])

        # create new key-value node
        self.cache[key] = Node(key, value)
        self.insert_node_end(self.cache[key])

        # remove lru (after head) if capacity exceeded
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove_node(lru)
            del self.cache[lru.key]

    