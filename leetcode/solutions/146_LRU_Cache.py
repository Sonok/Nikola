class Node:
    def __init__(self, key:int, val: int, next: "Node | None" = None, prev: "Node | None" = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.kv = {}
        self.capacity = capacity
        self.head = None # this is a doubly linked list
        self.end = None
    
    def getSize(self):
        return len(self.kv)

    def get(self, key: int) -> int:
        if key in self.kv:
            self.deleteNode(self.kv[key])
            self.addFront(self.kv[key])
            return self.kv[key].val
        return -1 
        # if not in in the list return -1 

    def deleteNode(self, node:Node): # just delete the node
        if self.head == node and self.end == node:
            self.head = None
            self.end = None
        elif node == self.head: # this is a head value
            self.head = node.next
            node.prev = None # we unlink the back
        elif node == self.end: # delete end value
            node.prev.next = None
            self.end = node.prev
        
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
    
    
    def addFront(self, node: Node):
        if not self.head:
            self.head = node
            self.end = node
        else:
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node 

        
    def put(self, key: int, value: int) -> None:
        node = Node(key, value)  # initalize value 

        if not self.head: # no values put in it 
            self.addFront(node)
            self.kv[key] = node
            self.end = node
        
        elif key in self.kv: # no need to change size or anything 
            currNode = self.kv[key] # delete curr 
            self.deleteNode(currNode)
            self.addFront(node) # update to front
            self.kv[key] = node # update the value

        else:
            if self.getSize() == self.capacity: # evict 
                del self.kv[self.end.key] 
                self.deleteNode(self.end) # delete the end value
                self.addFront(node)
                self.kv[key] = node
    
            else:
                self.addFront(node)
                self.kv[key] = node



