# Pattern 4 — Arrays / Strings / Sliding Window (Day 7 — refresh day)

High-frequency everywhere; you've likely seen variants. Goal today is speed, not learning.
Two of these are confirmed-asked at Tesla: LC 3 and LC 1758.

## 1. Two Sum (Easy)
Dict value → index, one pass: check `target - x` before inserting x.

## 121. Best Time to Buy and Sell Stock (Easy)
Track min-so-far; answer = max(price - min_so_far). One pass, O(1) space.

## 53. Maximum Subarray (Medium)
Kadane: `cur = max(x, cur + x); best = max(best, cur)`. Be ready to explain WHY (a negative
prefix never helps) — interviewers probe for understanding vs. memorization.

## 56. Merge Intervals (Medium)
Sort by start; extend `last[1] = max(last[1], cur[1])` when `cur[0] <= last[1]`, else append.
Team-relevant framing: merging overlapping alert windows.

## 3. Longest Substring Without Repeating Characters (Medium) — CONFIRMED ASKED
Sliding window, dict char → last index:
```python
def lengthOfLongestSubstring(s):
    last, left, best = {}, 0, 0
    for i, c in enumerate(s):
        if c in last and last[c] >= left:
            left = last[c] + 1
        last[c] = i
        best = max(best, i - left + 1)
    return best
```

## 347. Top K Frequent Elements (Medium)
`Counter` + `heapq.nlargest(k, count, key=count.get)`. Mention bucket sort for O(n).
Team-relevant: top-K most frequent alert codes across the fleet.

## 15. 3Sum (Medium)
Sort; fix i (skip duplicates); two pointers inward; skip duplicates on l/r after a hit.

## 1758. Min Changes to Make Alternating Binary (Easy) — CONFIRMED ASKED
Count mismatches vs pattern "0101..."; answer = min(mismatch, n - mismatch). 10 minutes, move on.

## 128. Longest Consecutive Sequence (Medium)
Set; only start counting when `x - 1 not in s` (that's the O(n) trick).

## 242. Valid Anagram (Easy) — `Counter(s) == Counter(t)`. Know the sorted() alternative.
## 202. Happy Number (Easy) — seen-set, or Floyd cycle detection (mention it).
## 392. Is Subsequence (Easy) — two pointers. Follow-up (many queries): binary search over
   precomputed char→indices lists — say it.
## 48. Rotate Image (Medium) — transpose then reverse each row. In place.
## 11. Container With Most Water (Medium) — two pointers, move the shorter wall.
## 767. Reorganize String (Medium) — max-heap of counts; pop two, append, re-push. Impossible
   if max count > (n+1)//2.
## 17. Letter Combinations of Phone Number (Medium) — backtracking template; also the
   itertools.product one-liner (write backtracking, mention product).
## 223. Rectangle Area (Medium) — A1 + A2 − overlap; overlap dims = max(0, min(r) − max(l)).
