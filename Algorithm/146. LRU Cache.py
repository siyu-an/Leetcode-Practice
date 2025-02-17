class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def addNode(self, newnode):
        temp = self.head.next
        newnode.next = temp
        newnode.prev = self.head
        self.head.next = newnode
        temp.prev = newnode
    def delNode(self, exnode):
        prev = exnode.prev
        next = exnode.next
        prev.next = next
        next.prev = prev
    

    def get(self, key: int) -> int:
        if key in self.cache:
            resNode = self.cache[key]
            ans = resNode.val
            del self.cache[key]
            self.delNode(resNode)
            self.addNode(resNode)
            self.cache[key] = self.head.next
            return ans
        return -1
    
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            resNode = self.cache[key]
            del self.cache[key]
            self.delNode(resNode)
        if len(self.cache) == self.size:
            del self.cache[self.tail.prev.key]
            self.delNode(self.tail.prev)
        self.addNode(self.Node(key,value))
        self.cache[key] = self.head.next