from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        n = len(senate)

        for i, ch in enumerate(senate):
            if ch == 'R':
                r.append(i)
            else:
                d.append(i)

        while r and d:
            ri = r.popleft()
            di = d.popleft()

            if ri < di:
                r.append(ri + n)
            else:
                d.append(di + n)

        return "Radiant" if r else "Dire"