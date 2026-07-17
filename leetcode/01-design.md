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

## 341. Flatten Nested List Iterator (Medium) — second pass if time
Stack of reversed items; `hasNext()` unwraps lists until top is an integer. Lazy evaluation
talking point: don't flatten upfront if the stream is huge.

## 2502. Design Memory Allocator (Medium) — second pass if time
Small constraints → brute-force array of owner-ids is accepted: allocate = scan for run of k
zeros, fill with mID; free = zero out all cells owned by mID. Say the interval-based optimization
exists; write the simple one.
