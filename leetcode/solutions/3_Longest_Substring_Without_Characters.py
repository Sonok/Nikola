class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
            
        longest = 1

        seen = set() # keep a running window that keeps all 
        # unique letters we see from l to r. window size is r-l + 1
        # might need a following left
        
        l = 0
        for r in range(n):

            if s[r] in seen:
                while(s[l] != s[r]):
                    seen.discard(s[l])
                    l += 1 # increment the loop 

                seen.discard(s[l])
                l += 1
                # now we have a clean window 

            seen.add(s[r])
            longest = max(longest, r-l+1)

        return longest
        