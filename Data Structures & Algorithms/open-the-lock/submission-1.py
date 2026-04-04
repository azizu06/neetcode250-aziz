class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        q = deque([("0000",0)])
        visit = set()
        while q:
            lock, turn = q.popleft()
            if lock in dead or lock in visit: continue
            if lock == target: return turn
            visit.add(lock)
            for i in range(4):
                lst = list(lock)
                lst[i] = str((int(lst[i])+1)%10)
                new = "".join(lst)
                q.append((new,turn+1))
                lst = list(lock)
                lst[i] = str((int(lst[i])-1)%10)
                new = "".join(lst)
                q.append((new,turn+1))
        return -1




