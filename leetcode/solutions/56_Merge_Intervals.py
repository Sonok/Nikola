import heapq
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        heapq.heapify(intervals)
        out = []
        start, end = heapq.heappop(intervals)
        
        while intervals:
            s, e = heapq.heappop(intervals)
            if end >= s: # we might be able to extend the end time so the start time of the 
            # next event overlaps the with end of prev event 
                end = max(end, e) # see which end is longer
            else:
                out.append([start, end])
                start, end = s, e

        
        out.append([start, end]) # the last interval doesn't get added because 
        # in the loop we only add the element when we see another interval 
        # that doesn't intersect with the current interval. The problem is we hit the end
        return out

