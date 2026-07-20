from collections import defaultdict, deque
class Logger:

    def __init__(self):
        self.msg_queue = deque() # string, times
        self.msg_set = set() # efficent look up on deque message

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while(self.msg_queue and self.msg_queue[0][1] <= timestamp - 10):  # out of frame
            msg, ts = self.msg_queue.popleft()
            self.msg_set.discard(msg)
        
        if message in self.msg_set:# inscope 
            return False
        
        self.msg_set.add(message)
        self.msg_queue.append((message, timestamp))
        
        return True 


 
