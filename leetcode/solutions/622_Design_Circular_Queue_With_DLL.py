class Node:
    def __init__(self, val:int, next: "Node | None" = None, prev: "Node | None" = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = None 
        self.end = None
        self.size = 0
        self.capacity = k # fixed

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False # finish nothing to do
        
        if self.isEmpty():
            self.front = Node(value, None, None)
            self.end = self.front
            self.size = 1 
            return True 

        n = Node(value, None, self.end) # so now this last node is link
        self.end.next = n # now linking last node
        self.end = n
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False # finish nothing to do
        # front is same as back otherwise we don't touch the front
        if self.front == self.end:
            self.front = None
            self.end = None 
            self.size = 0
            return True
        
        self.front = self.front.next
        self.front.prev = None
        self.size -= 1

        return True



    def Front(self) -> int:
        if self.front:
            return self.front.val
        return -1

    def Rear(self) -> int:
        if self.front:
            return self.end.val
        return -1

    def isEmpty(self) -> bool:
        return not self.front

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()