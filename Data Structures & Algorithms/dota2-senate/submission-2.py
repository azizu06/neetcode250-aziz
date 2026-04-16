class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        freq = Counter(senate)
        q = deque(senate)
        while len(q) > 1:
            s = q[0]
            target = 'D' if s == 'R' else 'R'
            cnt = 0
            while q[0] == s:
                q.append(q.popleft())
                cnt+=1
            freq[target]-=cnt
            if freq[target] <= 0: return 'Dire' if target == 'R' else 'Radiant'
            while q[0] == target and cnt:
                q.popleft()
                cnt-=1
        return "Radiant" if q[0] == 'R' else "Dire"