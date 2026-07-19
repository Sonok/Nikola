import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums 
            
        c = Counter(nums)
        lst = [(-c[x], x) for x in c]
        heapq.heapify(lst)

        out = []

        while k: 
            out.append(heapq.heappop(lst)[1])
            k -= 1
        
        return out
