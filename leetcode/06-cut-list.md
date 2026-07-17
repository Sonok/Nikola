# Cut list — only if ahead of schedule

With ~10 days, these are deliberately dropped. 25 questions cold > 42 shaky.
If you find spare hours, pull back in THIS order:

1. **42. Trapping Rain Water (Hard)** — most likely of the cut to appear. Two pointers,
   move the side with the smaller max; water at i = min(maxL, maxR) − h[i].
2. **399. Evaluate Division** — covered in 03-graphs.md; do it if the graph days go fast.
3. **41. First Missing Positive (Hard)** — cyclic sort: put x at index x−1 by swapping;
   first i where a[i] != i+1. O(n)/O(1).
4. **4. Median of Two Sorted Arrays (Hard)** — binary search the partition of the shorter
   array. Low intern frequency; understand the invariant even if you don't drill it.
5. **127. Word Ladder (Hard)** — BFS with wildcard buckets (sketch in 03-graphs.md).
6. **341 / 2502** — design second-passers (sketches in 01-design.md).

**Skip entirely: 126. Word Ladder II.** Hardest on the list, lowest ask-rate, biggest time pit.
Know the one-sentence approach (BFS parent-DAG + backtrack) and nothing more.

Everything else on the tag list (11, 128, 242, 202, 392, 767, 48, 17, 223, 1758, 3, ...) is
already covered in files 01–05.
