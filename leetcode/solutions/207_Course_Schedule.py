from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereqs = [0] * numCourses
        s = set(range(numCourses)) # visited 

        dic = defaultdict(list)


        # we should then process all their courses and their prereq
        for a, b in prerequisites:
            prereqs[a] += 1
            s.discard(a) # obv we can't finish a class with a prereq
            dic[b].append(a)
        
        if(len(s) == 0):
            return False
        q = deque(s) # this is our schedule for the year 
        # from here we only add to 
        while(q):
            course = q.popleft()
            for adj in dic[course]:
                prereqs[adj] -= 1
                if prereqs[adj] == 0: # you can finally take the course
                    s.add(adj)
                    q.append(adj)
            del dic[course]

        return len(s) == numCourses