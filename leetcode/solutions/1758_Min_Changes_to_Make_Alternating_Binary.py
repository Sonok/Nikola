class Solution:
    def minOperations(self, s: str) -> int:
        # you should do it greedily
        # 1010010101
        # 0101010101 altenrate 4
        # 1010101010 that's 6 so that doesn't work 

         # start with 0s 
        zeroFlip = 0
        oneFlip = 0
        for i, c in enumerate(s):
            if (i % 2 == 0):
                if c == '1':
                    zeroFlip += 1 
                else:
                    oneFlip += 1
            else:
                if c == '1':
                    oneFlip += 1 
                else:
                    zeroFlip += 1
         # start with 1s 
        
        return min(oneFlip, zeroFlip)