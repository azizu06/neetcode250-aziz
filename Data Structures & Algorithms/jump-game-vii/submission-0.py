class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        far = 0
        while q:
            i = q.popleft()
            start = max(i+minJump,far+1)
            end = min(len(s),i+maxJump+1)
            for j in range(start,end):
                if s[j] == '0':
                    q.append(j)
                    if j == len(s)-1:
                        return True
            far = i+maxJump
        return False

    