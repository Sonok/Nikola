class Solution:

    def validUtf8(self, data: List[int]) -> bool:

        n = len(data)
        i = 0
        while(i < n):
            val = data[i]
            if val >> 7 == 0: # just go to the next digit none of the other sequences start with 0
                i += 1
                continue 
            countOnes = 0
            while(countOnes <= 4 and (val >> (7 - countOnes)) & 1):
                countOnes += 1 

            if countOnes == 1 or countOnes >= 5:
                return False # only 2,3,4 work 

            i += 1
            for _ in range(1, countOnes): # this many have to start with a 10
                if i < n and data[i] >> 6 == 2:
                    i += 1 
                else:
                    return False
            

        return True
            