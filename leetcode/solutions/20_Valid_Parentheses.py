class Solution:
    def isValid(self, s: str) -> bool:
        openCloseMap = {'(' :')','{' :'}' , '[' : ']'}
        stack = []
        for c in s:
            if c in openCloseMap:
                stack.append(openCloseMap[c])
            elif not stack:
                return False
            else:
                if stack[-1] != c:
                    return False
                else:
                    stack.pop()
        return not stack
