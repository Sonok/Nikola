# Pattern 1 — Design / OOP (Days 1–2)

Tesla's signature category: 7 of 42 tagged questions. These test clean class structure, dict/deque
fluency, and talking through trade-offs — exactly what a backend team wants to see. **LRU Cache is
the single most-reported Tesla question. Drill it until you can write it blank-editor in ~12 min.**

## The skeleton every design question shares
```python
class Thing:
    def __init__(self, ...):
        # choose your core structures OUT LOUD: dict for O(1) lookup,
        # deque for FIFO, heap for ordering, sets for membership
        ...
    def operation(self, ...) -> ...:
        # validate → mutate → return. Keep methods < 10 lines.
        ...
```
Interviewer signal: state the time complexity of every method unprompted.

---

## 146. LRU Cache (Medium) — THE Tesla question
O(1) get/put. Two canonical answers — know both, lead with OrderedDict, offer the linked list.

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.d.move_to_end(key)          # mark as most-recently-used
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.move_to_end(key)
        self.d[key] = value
        if len(self.d) > self.cap:
            self.d.popitem(last=False)   # evict least-recently-used
```
Follow-ups they ask: implement without OrderedDict (dict + doubly-linked list with dummy
head/tail — practice this version too), thread-safety (wrap ops in a `threading.Lock`),
TTL expiry (store `(value, expires_at)`, lazily evict on get).

## 359. Logger Rate Limiter (Easy)
Dict message → last-printed timestamp. `return ts - self.last.get(msg, -10) >= 10` then record.
Follow-up: memory grows forever → evict old entries with a deque of (ts, msg), or note this is
exactly a rate-limiter on an alerts pipeline (relevant to the team — say so).

## 1603. Design Parking System (Easy)
`self.slots = [0, big, medium, small]`; addCar decrements and returns `self.slots[carType] > 0`.
Two-minute question — the test is whether your code is clean, not clever.

## 622. Design Circular Queue (Medium)
Fixed array + head index + size counter (avoid the head/tail ambiguity bug):
```python
class MyCircularQueue:
    def __init__(self, k):
        self.a, self.k, self.head, self.n = [0] * k, k, 0, 0
    def enQueue(self, v):
        if self.n == self.k: return False
        self.a[(self.head + self.n) % self.k] = v
        self.n += 1
        return True
    def deQueue(self):
        if self.n == 0: return False
        self.head = (self.head + 1) % self.k
        self.n -= 1
        return True
    def Front(self): return -1 if self.n == 0 else self.a[self.head]
    def Rear(self):  return -1 if self.n == 0 else self.a[(self.head + self.n - 1) % self.k]
    def isEmpty(self): return self.n == 0
    def isFull(self):  return self.n == self.k
```
Talking point: this is a ring buffer — the core structure of telemetry/log ingestion.

## 348. Design Tic-Tac-Toe (Medium)
Don't scan the board. Per player keep `rows[n]`, `cols[n]`, `diag`, `anti` counters; a move wins
when any counter hits n. O(1) per move. (Use +1 for player 1, -1 for player 2 on shared counters.)

## 588. Design In-Memory File System (Hard) — ⚠ FIRSTHAND REPORT: asked last cycle
Not on the public tag list, but a friend was explicitly asked this in a Tesla interview last
cycle. Treat it as Tier 1 — drill it right after LRU Cache. It's the design pattern at its
biggest: a tree of nodes + path parsing + clean class structure.

Key insight: one node type for both files and directories keeps the code short.

```python
class Node:
    def __init__(self):
        self.children = {}       # name -> Node (empty for files)
        self.content = ""        # non-empty only for files
        self.is_file = False

class FileSystem:
    def __init__(self):
        self.root = Node()

    def _walk(self, path):                    # "/a/b/c" -> node, creating dirs on the way
        node = self.root
        if path == "/":
            return node
        for part in path.strip("/").split("/"):
            node = node.children.setdefault(part, Node())
        return node

    def ls(self, path: str) -> list[str]:
        node = self._walk(path)
        if node.is_file:
            return [path.rstrip("/").split("/")[-1]]   # ls on a file -> just its name
        return sorted(node.children)

    def mkdir(self, path: str) -> None:
        self._walk(path)                       # setdefault creates the whole chain

    def addContentToFile(self, path: str, content: str) -> None:
        node = self._walk(path)
        node.is_file = True
        node.content += content                # APPEND, not replace

    def readContentFromFile(self, path: str) -> str:
        return self._walk(path).content
```
Traps: `ls` on a file returns a one-element list with the file's NAME (not path, not content);
`ls` output must be sorted; `addContentToFile` appends. Complexity: O(path parts) per op,
O(n log n) for the sort in ls.

Follow-ups to be ready for (say them proactively if time remains):
- **delete/move**: delete needs the PARENT node — walk to parent, `del children[name]`;
  move = detach + attach. This is why some prefer `_walk` to return (parent, name).
- **permissions / metadata**: hang an attrs dict on Node.
- **concurrency**: coarse lock per FileSystem vs. lock striping per directory — tie to the
  concurrency emphasis this team reportedly has.
- **persistence**: this is a trie in memory; real FS = same tree serialized to blocks/inodes.
Related: LC 1166 Design File System (Medium) is the lighter version — good warmup if you
have 20 spare minutes.

## 341. Flatten Nested List Iterator (Medium) — second pass if time
Stack of reversed items; `hasNext()` unwraps lists until top is an integer. Lazy evaluation
talking point: don't flatten upfront if the stream is huge.

## 2502. Design Memory Allocator (Medium) — second pass if time
Small constraints → brute-force array of owner-ids is accepted: allocate = scan for run of k
zeros, fill with mID; free = zero out all cells owned by mID. Say the interval-based optimization
exists; write the simple one.
