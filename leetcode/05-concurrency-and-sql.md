# Pattern 5 — Concurrency + SQL (Day 8 — do not skip)

A concurrency question on a company tag list is a deliberate signal, and one Tesla intern offer
report said the team "prioritized design and concurrency; multithreading knowledge was essential."
Database questions are also confirmed inside Tesla intern coding rounds.

## 1117. Building H2O (Medium) — threading
Release oxygen only when 2 hydrogens are ready and vice versa. Cleanest: two semaphores + barrier.
```python
from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.h = Semaphore(2)     # at most 2 H per molecule
        self.o = Semaphore(1)     # at most 1 O per molecule
        self.bar = Barrier(3)     # all 3 atoms sync, then reset

    def hydrogen(self, releaseHydrogen):
        self.h.acquire()
        self.bar.wait()
        releaseHydrogen()
        self.h.release()

    def oxygen(self, releaseOxygen):
        self.o.acquire()
        self.bar.wait()
        releaseOxygen()
        self.o.release()
```
Concepts to be able to define cold: race condition, mutex vs semaphore (mutex = 1-permit
semaphore with ownership), deadlock's four conditions (mutual exclusion, hold-and-wait,
no preemption, circular wait) + how to break one, Python GIL (threads fine for I/O-bound —
which is exactly what backend services are; multiprocessing for CPU-bound).
Related warmups if you have 20 min: LC 1114 Print in Order, LC 1115 FooBar.

## 1729. Find Followers Count (Easy) — SQL
```sql
SELECT user_id, COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
```
15-minute refresh beyond this one: JOIN vs LEFT JOIN, GROUP BY + HAVING,
COUNT(DISTINCT), a window function example (ROW_NUMBER() OVER (PARTITION BY ...)),
and one index sentence: "B-tree index on the filter/join column turns a scan into a seek."
SQL vs NoSQL one-liner for the JD: relational for service appointments/parts (transactions,
joins); wide-column/time-series for telemetry and alert history (write volume, TTL, scans by
vehicle+time range).

## Day 8 second half — re-drills
1. LRU Cache from blank editor, target < 12 min.
2. Basic Calculator II from blank editor, target < 15 min.
3. Topo sort (Course Schedule) from blank editor, target < 12 min.
