from collections import defaultdict, deque
class Logger:

    def __init__(self):
        self.kv = defaultdict(int) # indicates a time stamp

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.kv:
            self.kv[message] = timestamp
            return True 
        
        if timestamp >= self.kv[message] + 10: # update
            self.kv[message] = timestamp
            return True

        return False

 


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)