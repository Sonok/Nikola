from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c = Counter(s)
        for char in t:
            if char not in c:
                return False
            c[char] -= 1
            if c[char] == 0:
                del c[char]
        return not c