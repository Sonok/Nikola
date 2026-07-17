# Pattern 3 — Graphs / BFS / DFS (Days 5–6)

8 of 42 tagged. A Course Schedule *variant* is a confirmed-asked Tesla intern question (in a round
that also had database questions). Two templates cover everything: grid BFS/DFS and topo sort.

## Template A — grid flood fill
```python
def neighbors(r, c, R, C):
    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            yield nr, nc
```

## Template B — topological sort (Kahn's / BFS)
```python
from collections import deque, defaultdict

def topo(n, edges):                      # edges: prereq -> course
    g, indeg = defaultdict(list), [0] * n
    for a, b in edges:
        g[a].append(b)
        indeg[b] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []   # empty ⇒ cycle
```

---

## 200. Number of Islands (Medium)
Count flood fills: for each '1', DFS/BFS and sink visited cells to '0'. O(RC).
Say the follow-ups before asked: islands in a stream → Union-Find (LC 305);
huge grid → process row-band at a time.

## 207. Course Schedule (Medium) — confirmed-asked territory
Template B verbatim: return `len(order) == n`. Know the DFS-coloring cycle-detection
alternative (white/gray/black) well enough to describe.

## 2115. Find All Possible Recipes (Medium)
Course Schedule re-skinned: ingredients → recipe edges; seed queue with `supplies`;
a recipe is craftable when its indegree hits 0 via supplied/crafted items.
Talking point: this is dependency resolution — same shape as "which diagnostic steps can run
given available signals."

## 399. Evaluate Division (Medium)
Weighted graph: a/b = 2 ⇒ edge a→b weight 2 and b→a weight 1/2. Query = DFS/BFS multiplying
weights along the path; -1 if unreachable. Watch: query of unknown variable, x/x = 1.

## 909. Snakes and Ladders (Medium)
BFS on squares 1..n² (unweighted shortest path = BFS, always say this). The whole problem is the
coordinate transform: square s → row = (s-1)//n from bottom, col flips on odd rows
(boustrophedon). Jump BEFORE enqueueing if the cell has a snake/ladder; you can't chain jumps.

## 934. Shortest Bridge (Medium)
Two phases: DFS to find + mark the first island (collect its cells), then multi-source BFS from
all those cells simultaneously until you touch the second island; depth = answer.
Multi-source BFS is the reusable idea — mention it by name.

## 127. Word Ladder (Hard) — only if ahead of schedule
BFS over words; neighbors via wildcard buckets ("h*t") precomputed in a dict — O(26·L) per word
naive works too. Bidirectional BFS is the optimization to mention.

## 126. Word Ladder II (Hard) — SKIP (time pit)
If asked, describe: BFS to build level-by-level parent DAG, then DFS backtrack to enumerate paths.
Do not attempt to write from scratch under time pressure.
