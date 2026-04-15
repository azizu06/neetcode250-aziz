class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = []
        n = len(gas)
        for i in range(n):
            if cost[i] > gas[i]: continue
            start.append(i)
        for s in start:
            tank = 0
            for i in range(n):
                cur = (s+i)%n
                tank += (gas[cur]-cost[cur])
                if tank < 0: break
            if tank >= 0: return s
        return -1
"""
[5,8,2,8]
[6,5,6,6]
"""